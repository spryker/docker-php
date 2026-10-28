# PHP-FPM

[![Docker Stars](https://img.shields.io/docker/stars/spryker/php.svg)](https://hub.docker.com/r/spryker/php)
[![Docker Pulls](https://img.shields.io/docker/pulls/spryker/php.svg)](https://hub.docker.com/r/spryker/php)

## Description

Extends official PHP Docker images with extensions and tools to be able to run Spryker.

* Based on official PHP images
  * `Alpine 3.23`
  * `Alpine 3.24`
  * `Debian "bookworm"`
* Platforms: `linux/amd64`, `linux/arm64`
* Users: `root`, `spryker`
* Working directory: `/data`
* Includes:
  * [PHP extensions](#php-extensions)
  * PostgreSQL client
  * MySQL client
  * CURL
  * OpenSSH client
  * Composer v2

> Note: Provided images require additional configuration for development, staging, and production use.

## Tags

| Tag                                                                                         | PHP version | Linux distribution | Dockerfile                                                                                 | OTEL support |
|:--------------------------------------------------------------------------------------------|:------------|:-------------------|:-------------------------------------------------------------------------------------------|:------------:|
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags?name=latest)                 | 8.2.35      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.2/Dockerfile)     |      ✖       |
| [spryker/php:8.5](https://hub.docker.com/r/spryker/php/tags?name=8.5)                       | 8.5.12      | Alpine 3.24        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.24/8.5/Dockerfile)     |      ✔       |
| [spryker/php:8.4](https://hub.docker.com/r/spryker/php/tags?name=8.4)                       | 8.4.27      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.4/Dockerfile)     |      ✔       |
| [spryker/php:8.3](https://hub.docker.com/r/spryker/php/tags?name=8.3)                       | 8.3.36      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.3/Dockerfile)     |      ✔       |
| [spryker/php:8.2](https://hub.docker.com/r/spryker/php/tags?name=8.2)                       | 8.2.35      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.2/Dockerfile)     |      ✖       |
| [spryker/php:8.5-alpine3.24](https://hub.docker.com/r/spryker/php/tags?name=8.5-alpine3.24) | 8.5.12      | Alpine 3.24        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.24/8.5/Dockerfile)     |      ✔       |
| [spryker/php:8.4-alpine3.24](https://hub.docker.com/r/spryker/php/tags?name=8.4-alpine3.24) | 8.4.27      | Alpine 3.24        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.24/8.4/Dockerfile)     |      ✔       |
| [spryker/php:8.3-alpine3.24](https://hub.docker.com/r/spryker/php/tags?name=8.3-alpine3.24) | 8.3.36      | Alpine 3.24        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.24/8.3/Dockerfile)     |      ✔       |
| [spryker/php:8.2-alpine3.24](https://hub.docker.com/r/spryker/php/tags?name=8.2-alpine3.24) | 8.2.35      | Alpine 3.24        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.24/8.2/Dockerfile)     |      ✖       |
| [spryker/php:8.4-alpine3.23](https://hub.docker.com/r/spryker/php/tags?name=8.4-alpine3.23) | 8.4.27      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.4/Dockerfile)     |      ✔       |
| [spryker/php:8.3-alpine3.23](https://hub.docker.com/r/spryker/php/tags?name=8.3-alpine3.23) | 8.3.36      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.3/Dockerfile)     |      ✔       |
| [spryker/php:8.2-alpine3.23](https://hub.docker.com/r/spryker/php/tags?name=8.2-alpine3.23) | 8.2.35      | Alpine 3.23        | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.23/8.2/Dockerfile)     |      ✖       |
| [spryker/php:8.5-debian](https://hub.docker.com/r/spryker/php/tags?name=8.5-debian)         | 8.5.12      | Debian "bookworm"  | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bookworm/8.5/Dockerfile) |      ✔       |
| [spryker/php:8.4-debian](https://hub.docker.com/r/spryker/php/tags?name=8.4-debian)         | 8.4.27      | Debian "bookworm"  | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bookworm/8.4/Dockerfile) |      ✔       |
| [spryker/php:8.3-debian](https://hub.docker.com/r/spryker/php/tags?name=8.3-debian)         | 8.3.36      | Debian "bookworm"  | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bookworm/8.3/Dockerfile) |      ✔       |
| [spryker/php:8.2-debian](https://hub.docker.com/r/spryker/php/tags?name=8.2-debian)         | 8.2.35      | Debian "bookworm"  | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bookworm/8.2/Dockerfile) |      ✔       |

### Discontinued tags

The `*-alpine3.21` and `*-alpine3.22` tags are no longer built. The official PHP images stopped publishing for these Alpine releases, so they remain on PHP versions without the October 2026 security fixes. Switch to the matching `-alpine3.23` or `-alpine3.24` tag.

## How to use

### Pull image
```bash
docker pull spryker/php
docker pull spryker/php:8.4
```

### Run container
```bash
docker run -i --rm spryker/php:latest php -v
```

### Dockerfile
```dockerfile
FROM spryker/php:8.4
```

### docker-compose.yml
```yaml
services:
  app:
    image: spryker/php:8.4-debian
```

### Enable optional extensions

The following extensions are built into every image but stay disabled. Their configuration files live in `/usr/local/etc/php/disabled/`.

| Extension   | Purpose                                                              |
|:------------|:---------------------------------------------------------------------|
| `amqp`      | RabbitMQ client                                                      |
| `blackfire` | Blackfire profiler probe, configured through `BLACKFIRE_*` variables |
| `excimer`   | Sampling profiler                                                    |
| `imagick`   | ImageMagick bindings                                                 |
| `newrelic`  | New Relic APM agent, configured through `NEWRELIC_*` variables       |
| `otel`      | OpenTelemetry with gRPC and Protobuf; see [Tags](#tags) for support  |
| `pcov`      | Code coverage driver                                                 |
| `tideways`  | Tideways profiler, configured through `TIDEWAYS_*` variables         |
| `xhprof`    | Hierarchical profiler                                                |
| `xlswriter` | Reads and writes XLSX files                                          |
| `xsl`       | XSLT transformations with `XSLTProcessor`                            |

To enable one, move its file into `conf.d`:
```dockerfile
FROM spryker/php:8.4

RUN mv /usr/local/etc/php/disabled/newrelic.ini /usr/local/etc/php/conf.d/90-newrelic.ini
```

With the [Spryker Docker SDK](https://github.com/spryker/docker-sdk), list them in the deploy file instead:
```yaml
image:
    tag: spryker/php:8.4
    php:
        enabled-extensions:
            - newrelic
```

## PHP extensions

```
Installed extensions
====================
  [x] bcmath
  [x] bz2
  [ ] calendar
  [ ] com_dotnet
  [x] ctype
  [x] curl
  [x] date
  [ ] dba
  [ ] dl_test
  [x] dom
  [ ] enchant
  [ ] exif
  [ ] ext_skel.php
  [ ] ffi
  [x] fileinfo
  [x] filter
  [x] ftp
  [x] gd
  [ ] gettext
  [x] gmp
  [x] hash
  [x] iconv
  [ ] imap
  [x] intl
  [x] json
  [ ] ldap
  [x] libxml
  [x] mbstring
  [x] mysqli
  [x] mysqlnd
  [ ] oci8
  [ ] odbc
  [x] opcache
  [x] openssl
  [x] pcntl
  [x] pcre
  [x] pdo
  [ ] pdo_dblib
  [ ] pdo_firebird
  [x] pdo_mysql
  [ ] pdo_oci
  [ ] pdo_odbc
  [x] pdo_pgsql
  [x] pdo_sqlite
  [x] pgsql
  [x] phar
  [x] posix
  [ ] pspell
  [x] random
  [x] readline
  [x] reflection
  [x] session
  [ ] shmop
  [x] simplexml
  [ ] skeleton
  [ ] snmp
  [x] soap
  [x] sockets
  [x] sodium
  [x] spl
  [x] sqlite3
  [x] standard
  [ ] sysvmsg
  [ ] sysvsem
  [ ] sysvshm
  [ ] tidy
  [x] tokenizer
  [x] xml
  [x] xmlreader
  [x] xmlwriter
  [ ] xsl
  [ ] zend_test
  [x] zip
  [x] zlib

Disabled extensions
====================
 [ ] amqp 2.2.0
 [ ] blackfire 1.92.48~linux-musl-x64-non_zts83
 [ ] excimer 1.2.6
 [ ] imagick 3.8.1
 [ ] newrelic 12.12.0.41
 [ ] otel 
 [ ] pcov 1.0.12
 [ ] tideways 5.47.0-e84e8a5
 [ ] xhprof 2.3.10
 [ ] xlswriter 3.0.0
 [ ] xsl 8.3.36

INSTALLED PACKAGES, CHANNEL PECL.PHP.NET:
=========================================
PACKAGE   VERSION STATE
amqp      2.2.0   stable
apcu      5.1.28  stable
excimer   1.2.6   stable
imagick   3.8.1   stable
pcov      1.0.12  stable
redis     6.3.0   stable
xdebug    3.5.3   stable
xhprof    2.3.10  stable
xlswriter 3.0.0   stable

Composer
====================
Composer version 2.10.3 2026-08-27 13:34:23
```

The report above is for `spryker/php:8.3`. Run the following to get it for any tag:
```bash
docker run -i --rm spryker/php:8.3 bash -s<<'EOF'
    docker-php-source extract
    echo "Installed extensions"
    echo "===================="
    for ext in $(ls /usr/src/php/ext); do 
        if php -r "exit(extension_loaded('$ext') || ('$ext' == 'opcache' && extension_loaded('Zend OPcache')) ? 0 : 1);" 2>/dev/null; then
            echo "  [x] $ext"
        else
            echo "  [ ] $ext"
        fi
    done
    echo ""
    echo "Disabled extensions"
    echo "===================="
    for f in /usr/local/etc/php/disabled/*.ini; do 
        if [ -f "$f" ]; then
            disabled=$(basename "$f" | sed -e 's/\.ini$//')
            version=$(PHP_INI_SCAN_DIR=:/usr/local/etc/php/disabled php -r "echo phpversion('${disabled}');" 2>/dev/null || echo "")
            echo " [ ] ${disabled} ${version}"
        fi
    done
    echo ""
    echo "INSTALLED PACKAGES, CHANNEL PECL.PHP.NET:"
    echo "========================================="
    pear list -c pecl 2>/dev/null || echo "No PECL packages found"
    echo ""
    echo "Composer"
    echo "===================="
    composer -V
EOF
```

## More information
* [Spryker documentation](https://docs.spryker.com)
* [PHP supported versions](https://www.php.net/supported-versions.php)
* [PHP official images](https://github.com/docker-library/php)
