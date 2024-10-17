#!/bin/bash

# Set variables
CURRENT_TAG=$1
PREVIOUS_TAG=$2

# Run the current image and capture output
docker run -i --rm "$CURRENT_TAG" sh -s <<'EOF' > current-output.txt
    # Output installed PHP extensions
    docker-php-source extract
    echo "Installed extensions"
    echo "===================="
    for ext in `ls /usr/src/php/ext`; do
        echo ' ' `php -r "if (extension_loaded('$ext' !== 'opcache' ? '$ext' : 'Zend OPcache')) { echo '[x] $ext'; } else { echo '[ ] $ext'; }"`;
    done

    # Output disabled PHP extensions
    echo ""
    echo "Disabled extensions"
    echo "===================="
    for f in /usr/local/etc/php/disabled/*.ini; do
        disabled=$(basename $f | sed -e 's/\.ini$//');
        echo " [ ] ${disabled} $(PHP_INI_SCAN_DIR=:/usr/local/etc/php/disabled php -r "echo phpversion('${disabled}');")";
    done

    # List installed PECL extensions
    echo ""
    echo "PECL extensions"
    echo "===================="
    pear list -c pecl

    # Output the Composer version
    echo ""
    echo "Composer"
    echo "===================="
    composer -V

    # List installed system packages
    echo ""
    echo "Installed system packages"
    echo "=========================="
    apk info -vv | sort
EOF

docker run -i --rm "$PREVIOUS_TAG" sh -s <<'EOF' > previous-output.txt
    # Output installed PHP extensions
    docker-php-source extract
    echo "Installed extensions"
    echo "===================="
    for ext in `ls /usr/src/php/ext`; do
        echo ' ' `php -r "if (extension_loaded('$ext' !== 'opcache' ? '$ext' : 'Zend OPcache')) { echo '[x] $ext'; } else { echo '[ ] $ext'; }"`;
    done

    # Output disabled PHP extensions
    echo ""
    echo "Disabled extensions"
    echo "===================="
    for f in /usr/local/etc/php/disabled/*.ini; do
        disabled=$(basename $f | sed -e 's/\.ini$//');
        echo " [ ] ${disabled} $(PHP_INI_SCAN_DIR=:/usr/local/etc/php/disabled php -r "echo phpversion('${disabled}');")";
    done

    # List installed PECL extensions
    echo ""
    echo "PECL extensions"
    echo "===================="
    pear list -c pecl

    # Output the Composer version
    echo ""
    echo "Composer"
    echo "===================="
    composer -V

    # List installed system packages
    echo ""
    echo "Installed system packages"
    echo "=========================="
    apk info -vv | sort
EOF

# Compare the outputs
if [ -f previous-output.txt ]; then
    echo "Comparing current and previous outputs..."
    diff previous-output.txt current-output.txt || true
else
    echo "No previous output to compare."
fi
