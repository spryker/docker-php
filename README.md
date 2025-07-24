# PHP-FPM

[![Docker Stars](https://img.shields.io/docker/stars/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![Docker Pulls](https://img.shields.io/docker/pulls/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)

# Description

Extends official PHP Docker images with extensions and tools to be able to run Spryker.

* Based on official PHP images
  * `Alpine 3.17`
  * `Alpine 3.18`
  * `Alpine 3.19`
  * `Alpine 3.20`
  * `Debian "bullseye"`
  
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
| Tag                                                                                         | PHP version | Linux distribution | Details                                                                                                                                                                                    | Dockerfile                                                                                 |
|:--------------------------------------------------------------------------------------------|:------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags?name=latest)                 | 8.2.25      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:latest.svg)](https://microbadger.com/images/spryker/php:latest "Get your own image badge on microbadger.com")                 | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.2/Dockerfile)     |
| [spryker/php:8.3](https://hub.docker.com/r/spryker/php/tags?name=8.3)                       | 8.3.13      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:8.3.svg)](https://microbadger.com/images/spryker/php:8.3 "Get your own image badge on microbadger.com")                       | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.3/Dockerfile)     |
| [spryker/php:8.2](https://hub.docker.com/r/spryker/php/tags?name=8.2)                       | 8.2.25      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:8.2.svg)](https://microbadger.com/images/spryker/php:8.2 "Get your own image badge on microbadger.com")                       | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.2/Dockerfile)     |
| [spryker/php:8.1](https://hub.docker.com/r/spryker/php/tags?name=8.1)                       | 8.1.30      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1.svg)](https://microbadger.com/images/spryker/php:8.1 "Get your own image badge on microbadger.com")                       | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.1/Dockerfile)     |
| [spryker/php:8.3-alpine3.20](https://hub.docker.com/r/spryker/php/tags?name=8.3-alpine3.20) | 8.3.13      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:8.3-alpine3.20.svg)](https://microbadger.com/images/spryker/php:8.3-alpine3.20 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.3/Dockerfile)     |
| [spryker/php:8.2-alpine3.20](https://hub.docker.com/r/spryker/php/tags?name=8.2-alpine3.20) | 8.2.25      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:8.2-alpine3.20.svg)](https://microbadger.com/images/spryker/php:8.2-alpine3.20 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.2/Dockerfile)     |
| [spryker/php:8.1-alpine3.20](https://hub.docker.com/r/spryker/php/tags?name=8.1-alpine3.20) | 8.1.30      | Alpine 3.20        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-alpine3.20.svg)](https://microbadger.com/images/spryker/php:8.1-alpine3.20 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.20/8.1/Dockerfile)     |
| [spryker/php:8.3-alpine3.19](https://hub.docker.com/r/spryker/php/tags?name=8.3-alpine3.19) | 8.3.13      | Alpine 3.19        | [![](https://images.microbadger.com/badges/image/spryker/php:8.3-alpine3.19.svg)](https://microbadger.com/images/spryker/php:8.3-alpine3.19 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.19/8.3/Dockerfile)     |
| [spryker/php:8.2-alpine3.19](https://hub.docker.com/r/spryker/php/tags?name=8.2-alpine3.19) | 8.2.25      | Alpine 3.19        | [![](https://images.microbadger.com/badges/image/spryker/php:8.2-alpine3.19.svg)](https://microbadger.com/images/spryker/php:8.2-alpine3.19 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.19/8.2/Dockerfile)     |
| [spryker/php:8.1-alpine3.20](https://hub.docker.com/r/spryker/php/tags?name=8.1-alpine3.20) | 8.1.30      | Alpine 3.19        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-alpine3.19.svg)](https://microbadger.com/images/spryker/php:8.1-alpine3.19 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.19/8.1/Dockerfile)     |
| [spryker/php:8.3-alpine3.18](https://hub.docker.com/r/spryker/php/tags?name=8.3-alpine3.18) | 8.3.7       | Alpine 3.18        | [![](https://images.microbadger.com/badges/image/spryker/php:8.3-alpine3.18.svg)](https://microbadger.com/images/spryker/php:8.3-alpine3.18 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.18/8.3/Dockerfile)     |
| [spryker/php:8.2-alpine3.18](https://hub.docker.com/r/spryker/php/tags?name=8.2-alpine3.18) | 8.2.19      | Alpine 3.18        | [![](https://images.microbadger.com/badges/image/spryker/php:8.2-alpine3.18.svg)](https://microbadger.com/images/spryker/php:8.2-alpine3.18 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.18/8.2/Dockerfile)     |
| [spryker/php:8.1-alpine3.18](https://hub.docker.com/r/spryker/php/tags?name=8.1-alpine3.18) | 8.1.28      | Alpine 3.18        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-alpine3.18.svg)](https://microbadger.com/images/spryker/php:8.1-alpine3.18 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.18/8.1/Dockerfile)     |
| [spryker/php:8.3-debian](https://hub.docker.com/r/spryker/php/tags?name=8.3-debian)         | 8.3.13      | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:8.3-debian.svg)](https://microbadger.com/images/spryker/php:8.3-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/8.3/Dockerfile) |
| [spryker/php:8.2-debian](https://hub.docker.com/r/spryker/php/tags?name=8.2-debian)         | 8.2.25      | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:8.2-debian.svg)](https://microbadger.com/images/spryker/php:8.2-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/8.2/Dockerfile) |
| [spryker/php:8.1-debian](https://hub.docker.com/r/spryker/php/tags?name=8.1-debian)         | 8.1.30      | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-debian.svg)](https://microbadger.com/images/spryker/php:8.1-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/8.1/Dockerfile) |
| [spryker/php:8.0-debian](https://hub.docker.com/r/spryker/php/tags?name=8.0-debian)         | 8.0.30      | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:8.0-debian.svg)](https://microbadger.com/images/spryker/php:8.0-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/8.0/Dockerfile) |
## How to use

### Pull image
```bash
$ docker pull spryker/php
$ docker pull spryker/php:8.3
```

### Run container
```bash
$ docker run -i --rm spryker/php:latest php -v
```

### Dockerfile
```dockerfile
FROM spryker/php:8.2
```

### docker-compose.yml
```yaml
service1:
    image: spryker/php:8.2-debian
```

### Enable NewRelic
```dockerfile
FROM spryker/php:8.2

RUN mv /usr/local/etc/php/disabled/newrelic.ini /usr/local/etc/php/conf.d/90-newrelic.ini
```

### Enable Blackfire
```dockerfile
FROM spryker/php:8.2

RUN mv /usr/local/etc/php/disabled/blackfire.ini /usr/local/etc/php/conf.d/90-blackfire.ini
```

### Enable Tideways
```dockerfile
FROM spryker/php:8.2

RUN mv /usr/local/etc/php/disabled/tideways.ini /usr/local/etc/php/conf.d/90-tideways.ini
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
 [ ] amqp 2.1.2
 [ ] blackfire 1.92.28~linux-musl-x64-non_zts82
 [ ] newrelic 11.2.0.15
 [ ] pcov 1.0.11
 [ ] tideways 5.5.14
 [ ] xhprof 2.3.10

INSTALLED PACKAGES, CHANNEL PECL.PHP.NET:
=========================================
PACKAGE VERSION STATE
amqp    2.1.2   stable
apcu    5.1.24  stable
pcov    1.0.11  stable
redis   6.1.0   stable
xdebug  3.3.2   stable
xhprof  2.3.10  stable

Composer
====================
PHP version 8.2.25 (/usr/local/bin/php)
Composer version 2.8.1 2024-10-04 11:31:01
```
##### Run the following to get the report
```bash
$ docker run -i --rm spryker/php:latest bash -s<<'EOF'
    docker-php-source extract
    echo "Installed extensions";
    echo "====================";
    for ext in `ls /usr/src/php/ext`; do echo ' ' `php -r "if (extension_loaded('$ext' !== 'opcache' ? '$ext' : 'Zend OPcache')) { echo '[x] $ext'; } else { echo '[ ] $ext'; }"`; done
    echo "";
    echo "Disabled extensions";
    echo "====================";
    for f in /usr/local/etc/php/disabled/*.ini; do disabled=$(basename $f | sed -e 's/\.ini$//'); echo " [ ] ${disabled} $(PHP_INI_SCAN_DIR=:/usr/local/etc/php/disabled php -r "echo phpversion('${disabled}');")"; done
    echo "";
    pear list -c pecl
    echo "";
    echo "Composer";
    echo "====================";
    composer -V
EOF
```

## More information
* [Spryker documentation](https://documentation.spryker.com)
* [PHP supported versions](http://php.net/supported-versions.php)
* [PHP official images](https://github.com/docker-library/php)
