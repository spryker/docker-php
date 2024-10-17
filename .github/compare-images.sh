#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: No tag provided. Usage: ./compare-image.sh <docker-tag>"
  exit 1
fi

IMAGE_TAG=$1

if [[ "$IMAGE_TAG" == *"debian"* ]]; then
  docker run -i --rm "$IMAGE_TAG" sh -s <<'EOF'
      echo "=== Debian Version ==="
      echo -n "Debian " && cat /etc/debian_version

      echo ""
      echo "=== Installed PHP Extensions ==="
      docker-php-source extract
      for ext in `ls /usr/src/php/ext`; do
          echo ' ' `php -r "if (extension_loaded('$ext' !== 'opcache' ? '$ext' : 'Zend OPcache')) { echo '[x] $ext'; } else { echo '[ ] $ext'; }"`;
      done

      echo ""
      echo "=== Disabled PHP Extensions ==="
      for f in /usr/local/etc/php/disabled/*.ini; do
          disabled=$(basename $f | sed -e 's/\.ini$//');
          echo " [ ] ${disabled} $(PHP_INI_SCAN_DIR=:/usr/local/etc/php/disabled php -r "echo phpversion('${disabled}');")";
      done

      echo ""
      echo "=== PECL Extensions ==="
      pear list -c pecl

      echo ""
      echo "=== Composer Version ==="
      composer -V

      echo ""
      echo "=== Installed System Packages ==="
      dpkg-query -W --showformat='${Package} ${Version}\n' | sort
EOF
else
  docker run -i --rm "$IMAGE_TAG" sh -s <<'EOF'
      echo "=== Alpine Version ==="
      echo -n "Alpine " && cat /etc/alpine-release

      echo ""
      echo "=== Installed PHP Extensions ==="
      docker-php-source extract
      for ext in `ls /usr/src/php/ext`; do
          echo ' ' `php -r "if (extension_loaded('$ext' !== 'opcache' ? '$ext' : 'Zend OPcache')) { echo '[x] $ext'; } else { echo '[ ] $ext'; }"`;
      done

      echo ""
      echo "=== Disabled PHP Extensions ==="
      for f in /usr/local/etc/php/disabled/*.ini; do
          disabled=$(basename $f | sed -e 's/\.ini$//');
          echo " [ ] ${disabled} $(PHP_INI_SCAN_DIR=:/usr/local/etc/php/disabled php -r "echo phpversion('${disabled}');")";
      done

      echo ""
      echo "=== PECL Extensions ==="
      pear list -c pecl

      echo ""
      echo "=== Composer Version ==="
      composer -V

      echo ""
      echo "=== Installed System Packages ==="
      apk info -vv | sort
EOF
fi

