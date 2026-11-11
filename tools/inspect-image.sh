#!/bin/bash
#
# Shows how an image was built and what it is based on, without pulling it:
#   - PHP version and creation date (image config)
#   - source repository, commit, Dockerfile and CI run (BuildKit provenance attestation)
#   - upstream base image with the digest used at build time and its OS version
#   - whether the base image tag has moved on since the build
#   - Docker Hub tags pointing to the image and whether its floating tags have moved on
#
# Usage: ./tools/inspect-image.sh <image>
#   ./tools/inspect-image.sh spryker/php@sha256:b637dbbaa94ccf4149320be20066c19bb735e4e94c8a43351a1ae3dd7253e29b
#   ./tools/inspect-image.sh spryker/php:8.4
#
# Requires: docker (with buildx), jq, curl.

set -euo pipefail

if [ -z "${1:-}" ]; then
  echo "Error: No image provided. Usage: ./inspect-image.sh <image>"
  exit 1
fi

IMAGE=$1
MAX_TAG_PAGES=30

for cmd in docker jq curl; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Error: '$cmd' is required."
    exit 1
  fi
done

TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

inspect() {
  docker buildx imagetools inspect "$1" --format "$2"
}

field() {
  printf '  %-12s %s\n' "$1:" "$2"
}

# Resolves an image reference to its current digest, cached per reference.
current_digest() {
  local cache="$TMP_DIR/digest-${1//[^a-zA-Z0-9]/_}"
  if [ ! -f "$cache" ]; then
    inspect "$1" '{{.Manifest.Digest}}' > "$cache" 2>/dev/null || : > "$cache"
  fi
  cat "$cache"
}

# Prints the OS release of an image for a platform, read from the rootfs layer in its history.
os_release() {
  local cache="$TMP_DIR/image-${1//[^a-zA-Z0-9]/_}.json"
  if [ ! -f "$cache" ]; then
    inspect "$1" '{{json .Image}}' > "$cache" 2>/dev/null || echo '{}' > "$cache"
  fi
  jq -r --arg p "$2" '
    (if has("config") then . else .[$p] // {} end) as $img
    | ([$img.history[]?.created_by // "" | select(test("alpine-minirootfs-|debian\\.sh"))] | first // "") as $cmd
    | if ($cmd | test("alpine-minirootfs-")) then
        "Alpine " + ($cmd | capture("alpine-minirootfs-(?<v>[0-9.]+)-").v)
      elif ($cmd | test("debian\\.sh")) then
        $cmd | capture("out/ \\W*(?<suite>[a-z]+)\\W* \\W*@(?<ts>[0-9]+)")
        | "Debian \(.suite) (snapshot \(.ts | tonumber | todate | .[0:10]))"
      else
        "unknown"
      end' "$cache"
}

DIGEST=$(inspect "$IMAGE" '{{.Manifest.Digest}}')
inspect "$IMAGE" '{{json .Image}}' > "$TMP_DIR/image.raw.json"
inspect "$IMAGE" '{{json .Provenance}}' > "$TMP_DIR/provenance.raw.json"

# A single-platform manifest returns its config directly instead of a per-platform map.
# Attestations and Docker Hub tags refer to the multi-arch index, not to such a manifest.
SINGLE_PLATFORM=$(jq -r 'has("config")' "$TMP_DIR/image.raw.json")
jq 'if has("config") then {(.os + "/" + .architecture + (if .variant then "/" + .variant else "" end)): .} else . end' \
  "$TMP_DIR/image.raw.json" > "$TMP_DIR/image.json"
PLATFORMS=$(jq -r 'keys[]' "$TMP_DIR/image.json")
jq --arg p "${PLATFORMS%%$'\n'*}" 'if has("SLSA") then {($p): .} else . end' \
  "$TMP_DIR/provenance.raw.json" > "$TMP_DIR/provenance.json"

echo "Image:     $IMAGE"
echo "Digest:    $DIGEST"
echo "Platforms:" $PLATFORMS

for platform in $PLATFORMS; do
  # Supports both SLSA v1 (buildDefinition/runDetails) and v0.2 (invocation/materials) provenance.
  jq --arg p "$platform" --slurpfile prov "$TMP_DIR/provenance.json" '
    .[$p] as $img
    | ($prov[0][$p].SLSA // {}) as $slsa
    | ($slsa.buildDefinition.externalParameters.configSource // $slsa.invocation.configSource // {}) as $src
    | {
        created: ($img.created // ""),
        php: ([$img.config.Env[]? | select(startswith("PHP_VERSION="))] | first // "" | sub("^PHP_VERSION="; "")),
        has_provenance: ($slsa != {}),
        source: ($src.uri // ""),
        dockerfile: ($src.path // ""),
        builder: ($slsa.runDetails.builder.id // $slsa.builder.id // ""),
        bases: [($slsa.buildDefinition.resolvedDependencies // $slsa.materials // [])[]
          | select(.uri | startswith("pkg:docker/"))
          | select(.uri | test("^pkg:docker/docker/dockerfile") | not)
          | (.uri | sub("^pkg:docker/"; "") | sub("[?#].*$"; "")) as $ref
          | {name: ($ref | sub("@.*$"; "")), version: ($ref | sub("^[^@]*@"; "")), digest: ("sha256:" + .digest.sha256)}]
      }' "$TMP_DIR/image.json" > "$TMP_DIR/summary.json"

  echo ""
  echo "=== $platform ==="
  field "Created" "$(jq -r '.created' "$TMP_DIR/summary.json")"
  field "PHP" "$(jq -r '.php' "$TMP_DIR/summary.json")"

  if [ "$(jq -r '.has_provenance' "$TMP_DIR/summary.json")" != "true" ]; then
    if [ "$SINGLE_PLATFORM" == "true" ]; then
      echo "  No provenance attestation found. Attestations are attached to the multi-arch index,"
      echo "  so pass the index digest or a tag rather than a single-platform manifest digest."
    else
      echo "  No provenance attestation found (the image was built without one)."
    fi
    continue
  fi

  field "Source" "$(jq -r '.source' "$TMP_DIR/summary.json")"
  field "Dockerfile" "$(jq -r '.dockerfile' "$TMP_DIR/summary.json")"
  field "Builder" "$(jq -r '.builder' "$TMP_DIR/summary.json")"

  jq -r '.bases[] | [.name, .version, .digest] | @tsv' "$TMP_DIR/summary.json" > "$TMP_DIR/bases.tsv"
  while IFS=$'\t' read -r name version digest; do
    if [[ "$version" == sha256:* ]]; then
      field "Base image" "$name@$version"
    else
      field "Base image" "$name:$version@$digest"
    fi
    field "Base OS" "$(os_release "$name@$digest" "$platform")"

    if [[ "$version" == sha256:* ]]; then
      field "Base status" "pinned by digest"
      continue
    fi
    now=$(current_digest "$name:$version")
    if [ -z "$now" ]; then
      field "Base status" "unknown ($name:$version could not be resolved)"
    elif [ "$now" == "$digest" ]; then
      field "Base status" "up to date"
    else
      field "Base status" "outdated ($name:$version now points to $now)"
    fi
  done < "$TMP_DIR/bases.tsv"
done

# Docker Hub tags are only looked up for images hosted on Docker Hub.
REPO=${IMAGE%%@*}
if [[ "${REPO##*/}" == *:* ]]; then
  REPO=${REPO%:*}
fi
REPO=${REPO#docker.io/}
REPO=${REPO#index.docker.io/}
REGISTRY=${REPO%%/*}
if [[ "$REPO" == */* ]] && [[ "$REGISTRY" == *.* || "$REGISTRY" == *:* || "$REGISTRY" == "localhost" ]]; then
  exit 0
fi
if [[ "$REPO" != */* ]]; then
  REPO="library/$REPO"
fi

echo ""
echo "=== Docker Hub tags ($REPO) ==="

url="https://hub.docker.com/v2/repositories/$REPO/tags?page_size=100"
pages=0
: > "$TMP_DIR/tags.tsv"
while [ -n "$url" ] && [ "$pages" -lt "$MAX_TAG_PAGES" ]; do
  curl -fsS "$url" > "$TMP_DIR/page.json"
  jq -r '.results[] | [.name, (.digest // ""), ((.tag_last_pushed // .last_updated // "")[0:10])] | @tsv' \
    "$TMP_DIR/page.json" >> "$TMP_DIR/tags.tsv"
  url=$(jq -r '.next // empty' "$TMP_DIR/page.json")
  pages=$((pages + 1))
done
if [ -n "$url" ]; then
  echo "  Note: only the $((MAX_TAG_PAGES * 100)) most recently updated tags were checked."
fi

awk -F'\t' -v d="$DIGEST" '$2 == d' "$TMP_DIR/tags.tsv" > "$TMP_DIR/matching.tsv"
if [ ! -s "$TMP_DIR/matching.tsv" ]; then
  if [ "$SINGLE_PLATFORM" == "true" ]; then
    echo "  No tags point to this digest (tags point to the multi-arch index digest)."
  else
    echo "  No tags point to this digest (it may have been untagged or cleaned up)."
  fi
  exit 0
fi

while IFS=$'\t' read -r tag _ pushed; do
  printf '  %-60s pushed %s\n' "$tag" "$pushed"
done < "$TMP_DIR/matching.tsv"

# Commit-pinned tags (<tag>-<40 char sha>) have a floating counterpart (<tag>) that moves on every release.
echo ""
echo "=== Floating tags ==="
cut -f1 "$TMP_DIR/matching.tsv" | sed -E 's/-[0-9a-f]{40}$//' | sort -u > "$TMP_DIR/floating.txt"
while read -r tag; do
  line=$(awk -F'\t' -v t="$tag" '$1 == t' "$TMP_DIR/tags.tsv")
  if [ -z "$line" ]; then
    printf '  %-20s not found\n' "$tag"
    continue
  fi
  IFS=$'\t' read -r _ now pushed <<< "$line"
  if [ "$now" == "$DIGEST" ]; then
    printf '  %-20s current\n' "$tag"
  else
    printf '  %-20s outdated (now %s, pushed %s)\n' "$tag" "$now" "$pushed"
  fi
done < "$TMP_DIR/floating.txt"
