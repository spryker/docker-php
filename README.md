# PHP-FPM

[![Docker Stars](https://img.shields.io/docker/stars/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![Docker Pulls](https://img.shields.io/docker/pulls/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)

# Description

Extends official PHP Docker images with extensions and tools to be able to run Spryker on.

* Based on official PHP images
  * `Alpine 3.14`
  * `Alpine 3.15`
  * `Alpine 3.16`
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

> Note: Provided images require additional configuration for development, staging and production use.

## Tags

| Tag                                                                                               | PHP version | Linux distribution | Details                                                                                                                                                                                    | Dockerfile                                                                                 |
|:--------------------------------------------------------------------------------------------------|:------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags?name=latest)                       | 7.4.29      | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:latest.svg)](https://microbadger.com/images/spryker/php:latest "Get your own image badge on microbadger.com")                 | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/7.4/Dockerfile)     |
| [spryker/php:8.1](https://hub.docker.com/r/spryker/php/tags?name=8.1)                             | 8.1.6       | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1.svg)](https://microbadger.com/images/spryker/php:8.1 "Get your own image badge on microbadger.com")                       | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/8.1/Dockerfile)     |
| [spryker/php:8.0](https://hub.docker.com/r/spryker/php/tags?name=8.0)                             | 8.0.19      | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:8.0.svg)](https://microbadger.com/images/spryker/php:8.0 "Get your own image badge on microbadger.com")                       | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/8.0/Dockerfile)     |
| [spryker/php:7.4](https://hub.docker.com/r/spryker/php/tags?name=7.4)                             | 7.4.29      | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:7.4.svg)](https://microbadger.com/images/spryker/php:7.4 "Get your own image badge on microbadger.com")                       | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/7.4/Dockerfile)     |
| [spryker/php:8.1-alpine3.16](https://hub.docker.com/r/spryker/php/tags?name=8.1-alpine3.16)       | 8.1.8       | Alpine 3.16        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-alpine3.16.svg)](https://microbadger.com/images/spryker/php:8.1-alpine3.16 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.16/8.1/Dockerfile)     |
| [spryker/php:8.0-alpine3.16](https://hub.docker.com/r/spryker/php/tags?name=8.0-alpine3.16)       | 8.0.21      | Alpine 3.16        | [![](https://images.microbadger.com/badges/image/spryker/php:8.0-alpine3.16.svg)](https://microbadger.com/images/spryker/php:8.0-alpine3.16 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.16/8.0/Dockerfile)     |
| [spryker/php:7.4-alpine3.16](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.16)       | 7.4.30      | Alpine 3.16        | [![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.16.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.16 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.16/7.4/Dockerfile)     |
| [spryker/php:8.1-alpine3.15](https://hub.docker.com/r/spryker/php/tags?name=8.1-alpine3.15)       | 8.1.8       | Alpine 3.15        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-alpine3.15.svg)](https://microbadger.com/images/spryker/php:8.1-alpine3.15 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.15/8.1/Dockerfile)     |
| [spryker/php:8.0-alpine3.15](https://hub.docker.com/r/spryker/php/tags?name=8.0-alpine3.15)       | 8.0.21      | Alpine 3.15        | [![](https://images.microbadger.com/badges/image/spryker/php:8.0-alpine3.15.svg)](https://microbadger.com/images/spryker/php:8.0-alpine3.15 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.15/8.0/Dockerfile)     |
| [spryker/php:7.4-alpine3.15](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.15)       | 7.4.30      | Alpine 3.15        | [![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.15.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.15 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.15/7.4/Dockerfile)     |
| [spryker/php:8.1-alpine3.14](https://hub.docker.com/r/spryker/php/tags?name=8.0-alpine3.14)       | 8.1.6       | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-alpine3.14.svg)](https://microbadger.com/images/spryker/php:8.1-alpine3.14 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/8.1/Dockerfile)     |
| [spryker/php:8.0-alpine3.14](https://hub.docker.com/r/spryker/php/tags?name=8.0-alpine3.14)       | 8.0.19      | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:8.0-alpine3.14.svg)](https://microbadger.com/images/spryker/php:8.0-alpine3.14 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/8.0/Dockerfile)     |
| [spryker/php:7.4-alpine3.14](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.14)       | 7.4.29      | Alpine 3.14        | [![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.14.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.14 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.14/7.4/Dockerfile)     |
| [spryker/php:8.1-debian](https://hub.docker.com/r/spryker/php/tags?name=8.1-debian)               | 8.1.8       | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:8.1-debian.svg)](https://microbadger.com/images/spryker/php:8.1-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/8.1/Dockerfile) |
| [spryker/php:8.0-debian](https://hub.docker.com/r/spryker/php/tags?name=8.0-debian)               | 8.0.21      | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:8.0-debian.svg)](https://microbadger.com/images/spryker/php:8.0-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/8.0/Dockerfile) |
| [spryker/php:7.4-debian](https://hub.docker.com/r/spryker/php/tags?name=7.4-debian)               | 7.4.30      | Debian "bullseye"  | [![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com")         | [:link:](https://github.com/spryker/docker-php/blob/master/debian/bullseye/7.4/Dockerfile) |
## How to use

### Pull image
```bash
$ docker pull spryker/php
$ docker pull spryker/php:8.1
```

### Run container
```bash
$ docker run -i --rm spryker/php:latest php -v
```

### Dockerfile
```dockerfile
FROM spryker/php:8.1
```

### docker-compose.yml
```yaml
service1:
    image: spryker/php:8.1-debian
```

### Enable NewRelic
```dockerfile
FROM spryker/php:8.1

RUN mv /usr/local/etc/php/disabled/newrelic.ini /usr/local/etc/php/conf.d/90-newrelic.ini
```

### Enable Blackfire
```dockerfile
FROM spryker/php:8.1

RUN mv /usr/local/etc/php/disabled/blackfire.ini /usr/local/etc/php/conf.d/90-blackfire.ini
```

### Enable Tideways
```dockerfile
FROM spryker/php:8.1

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
 [ ] blackfire 1.80.0~linux-musl-x64-non_zts81
 [ ] newrelic 9.19.0.309
 [ ] tideways 5.5.8

INSTALLED PACKAGES, CHANNEL PECL.PHP.NET:
=========================================
PACKAGE VERSION STATE
apcu    5.1.22  stable
redis   5.3.7   stable
xdebug  3.1.6   stable

Composer
====================
Composer version 2.3.10 2022-07-13 15:48:23
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
