#!/bin/bash

diff_section() {
  section="$1"
  current_file="current-image-report.txt"
  previous_file="previous-image-report.txt"

  current_section=$(sed -n "/=== $section ===/,/=== /p" "$current_file" | sed '1d;$d')
  previous_section=$(sed -n "/=== $section ===/,/=== /p" "$previous_file" | sed '1d;$d')

  if [[ "$section" == "Installed System Packages" ]]; then
    diff_output=$(diff <(echo "$previous_section") <(echo "$current_section") | awk '
      BEGIN { FS = " - "; OFS = ": "; }
      function trim(s) { gsub(/^ +| +$/, "", s); return s }
      function clean_marker(s) { gsub(/^< |^> /, "", s); return s }
      function extract_pkg_and_description(line, pkg_version, description) {
        line = clean_marker(line);
        split(line, parts, " - ");
        pkg_version = trim(parts[1]);
        description = trim(parts[2]);
        return pkg_version ":" description;
      }
      /^</ {
        old_line = substr($0, 3);
        pkg_desc = extract_pkg_and_description(old_line);
        split(pkg_desc, parts, ":");
        old_pkg = parts[1];
        old_desc = parts[2];
        old_versions[old_desc] = old_pkg;
      }
      /^>/ {
        new_line = substr($0, 3);
        pkg_desc = extract_pkg_and_description(new_line);
        split(pkg_desc, parts, ":");
        new_pkg = parts[1];
        new_desc = parts[2];
        if (new_desc in old_versions) {
          print new_desc ": " old_versions[new_desc] " -> " new_pkg;
          delete old_versions[new_desc];
        } else {
          print new_desc ": (new) -> " new_pkg;
        }
      }
      END {
        for (desc in old_versions) {
          print desc ": " old_versions[desc] " -> (removed)";
        }
      }')
  else
    diff_output=$(diff <(echo "$previous_section") <(echo "$current_section") | awk '
      /^</ { old_line = substr($0, 3); }
      /^>/ { new_line = substr($0, 3); print old_line " -> " new_line; }')
  fi

  echo "$diff_output"
}

SECTIONS=("PHP Version" "Alpine Version" "Installed PHP Extensions" "Disabled PHP Extensions" "PECL Extensions" "Composer Version" "Installed System Packages")
FORMATTED_DIFF=""

for section in "${SECTIONS[@]}"; do
  section_diff=$(diff_section "$section")
  if [[ -n "$section_diff" ]]; then
    FORMATTED_DIFF+="=== $section ===\\n"
    FORMATTED_DIFF+="${section_diff//[$'\n']/\\n}\\n"
  fi
done

echo -e "Formatted Diff Output:\n$FORMATTED_DIFF"

echo "FORMATTED_DIFF<<EOF" >> $GITHUB_ENV
echo -e "$FORMATTED_DIFF" >> $GITHUB_ENV
echo "EOF" >> $GITHUB_ENV

#echo "step_id=$(echo $GITHUB_STEP_ID)" >> $GITHUB_OUTPUT
