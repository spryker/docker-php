# PHP-FPM

[![Docker Stars](https://img.shields.io/docker/stars/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![Docker Pulls](https://img.shields.io/docker/pulls/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![microbadger version](https://images.microbadger.com/badges/version/spryker/php.svg)](https://microbadger.com/images/spryker/php "Get your own version badge on microbadger.com")
[![microbadger image](https://images.microbadger.com/badges/image/spryker/php.svg)](https://microbadger.com/images/spryker/php "Get your own image badge on microbadger.com")

# Description

Extends official PHP Docker images with extensions and tools to be able to run Spryker on.

* Based on official PHP images
  * `Alpine 3.10`
  * `Alpine 3.11`
  * `Alpine 3.12`
  * `Debian "buster"`
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

| Tag | PHP version | Linux distribution | Details | Dockerfile |
| :------------- | :------------- | :------------- | :------------- | :------------- |
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags?name=latest) | 7.3.26 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:latest.svg)](https://microbadger.com/images/spryker/php:latest "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:8.0](https://hub.docker.com/r/spryker/php/tags?name=8.0)  | 8.0.5 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:8.0.svg)](https://microbadger.com/images/spryker/php:8.0 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/8.0/Dockerfile) |
| [spryker/php:7.4](https://hub.docker.com/r/spryker/php/tags?name=7.4)  | 7.4.16 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4.svg)](https://microbadger.com/images/spryker/php:7.4 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.4/Dockerfile) |
| [spryker/php:7.3](https://hub.docker.com/r/spryker/php/tags?name=7.3)  | 7.3.27 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3.svg)](https://microbadger.com/images/spryker/php:7.3 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:8.0-alpine3.13](https://hub.docker.com/r/spryker/php/tags?name=8.0-alpine3.13)  | 8.0.5 | Alpine 3.13 |[![](https://images.microbadger.com/badges/image/spryker/php:8.0-alpine3.13.svg)](https://microbadger.com/images/spryker/php:8.0-alpine3.13 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.13/8.0/Dockerfile) |
| [spryker/php:7.4-alpine3.13](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.13)  | 7.4.16 | Alpine 3.13 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.13.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.13 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.13/7.4/Dockerfile) |
| [spryker/php:8.0-alpine3.12](https://hub.docker.com/r/spryker/php/tags?name=8.0-alpine3.12)  | 8.0.5 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:8.0-alpine3.12.svg)](https://microbadger.com/images/spryker/php:8.0-alpine3.12 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/8.0/Dockerfile) |
| [spryker/php:7.4-alpine3.12](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.12)  | 7.4.16 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:8.0-alpine3.12.svg)](https://microbadger.com/images/spryker/php:8.0-alpine3.12 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/8.0/Dockerfile) |
| [spryker/php:7.3-alpine3.12](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.12)  | 7.3.27 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.12.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.12 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/7.3/Dockerfile) |
| [spryker/php:7.4-alpine3.11](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.11)  | 7.4.14 | Alpine 3.11 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.11.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.11 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.11/7.4/Dockerfile) |
| [spryker/php:7.3-alpine3.11](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.11)  | 7.3.26 | Alpine 3.11 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.11.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.11 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.11/7.3/Dockerfile) |
| [spryker/php:7.4-alpine3.10](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.10)  | 7.4.6 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.10.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.10 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.4/Dockerfile) |
| [spryker/php:7.3-alpine3.10](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.10)  | 7.3.18 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.10.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.10 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:8.0-debian](https://hub.docker.com/r/spryker/php/tags?name=8.0-debian)  | 8.0.5 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:8.0-debian.svg)](https://microbadger.com/images/spryker/php:8.0-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/8.0/Dockerfile) |
| [spryker/php:7.4-debian](https://hub.docker.com/r/spryker/php/tags?name=7.4-debian)  | 7.4.16 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.4/Dockerfile) |
| [spryker/php:7.3-debian](https://hub.docker.com/r/spryker/php/tags?name=7.3-debian)  | 7.3.27 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.3-debian.svg)](https://microbadger.com/images/spryker/php:7.3-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.3/Dockerfile) |
| [spryker/php:7.4-debian-buster](https://hub.docker.com/r/spryker/php/tags?name=7.4-debian-buster)  | 7.4.16 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.4/Dockerfile) |
| [spryker/php:7.3-debian-buster](https://hub.docker.com/r/spryker/php/tags?name=7.3-debian-buster)  | 7.3.27 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.3-debian.svg)](https://microbadger.com/images/spryker/php:7.3-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.3/Dockerfile) |

## How to use

### Pull image
```bash
$ docker pull spryker/php
$ docker pull spryker/php:7.4
```

### Run container
```bash
$ docker run -i --rm spryker/php:latest php -v
```

### Dockerfile
```dockerfile
FROM spryker/php:7.4
```

### docker-compose.yml
```yaml
service1:
    image: spryker/php:7.3-debian
```

### Enable NewRelic
```dockerfile
FROM spryker/php:7.4

RUN mv /usr/local/etc/php/disabled/newrelic.ini /usr/local/etc/php/conf.d/90-newrelic.ini
```

### Enable Blackfire
```dockerfile
FROM spryker/php:7.4

RUN mv /usr/local/etc/php/disabled/blackfire.ini /usr/local/etc/php/conf.d/90-blackfire.ini
```

### Enable Tideways
```dockerfile
FROM spryker/php:7.4

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
  [x] dom
  [ ] enchant
  [ ] exif
  [ ] ext_skel.php
  [x] fileinfo
  [x] filter
  [x] ftp
  [x] gd
  [ ] gettext
  [x] gmp
  [x] hash
  [x] iconv
  [ ] imap
  [ ] interbase
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
  [ ] recode
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
  [ ] wddx
  [x] xml
  [x] xmlreader
  [ ] xmlrpc
  [x] xmlwriter
  [ ] xsl
  [ ] zend_test
  [x] zip
  [x] zlib
Disabled extensions
====================
 [ ] blackfire 1.55.0
 [ ] newrelic 9.16.0.295
 [ ] tideways 5.3.14
Installed packages, channel pecl.php.net:
=========================================
Package Version State
apcu    5.1.20  stable
redis   5.3.4   stable
xdebug  3.0.3   stable
Composer
====================
Composer version 2.0.12 2021-04-01 10:14:59
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
