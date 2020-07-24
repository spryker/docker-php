# PHP-FPM

[![Docker Stars](https://img.shields.io/docker/stars/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![Docker Pulls](https://img.shields.io/docker/pulls/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![microbadger version](https://images.microbadger.com/badges/version/spryker/php.svg)](https://microbadger.com/images/spryker/php "Get your own version badge on microbadger.com")
[![microbadger image](https://images.microbadger.com/badges/image/spryker/php.svg)](https://microbadger.com/images/spryker/php "Get your own image badge on microbadger.com")

# Description

Extends official PHP Docker images with extensions and tools to be able to run Spryker on.

* Based on official PHP images
  * `Alpine 3.10`
  * `Debian "buster"`
* Users: `root`, `spryker`
* Working directory: `/data`
* Includes:
  * [PHP extensions](#php-extensions)
  * PostgreSQL client
  * MySQL client
  * CURL
  * OpenSSH client
  * Composer
  * `hirak/prestissimo`

> Note: Provided images require additional configuration for development, staging and production use.

## Tags

| Tag | PHP version | Linux distribution | Details | Dockerfile |
| :------------- | :------------- | :------------- | :------------- | :------------- |
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags?name=latest) | 7.3.20 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:latest.svg)](https://microbadger.com/images/spryker/php:latest "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:7.4](https://hub.docker.com/r/spryker/php/tags?name=7.4)  | 7.4.8 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4.svg)](https://microbadger.com/images/spryker/php:7.4 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.4/Dockerfile) |
| [spryker/php:7.3](https://hub.docker.com/r/spryker/php/tags?name=7.3)  | 7.3.20 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3.svg)](https://microbadger.com/images/spryker/php:7.3 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:7.2](https://hub.docker.com/r/spryker/php/tags?name=7.2)  | 7.2.32 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2.svg)](https://microbadger.com/images/spryker/php:7.2 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.2/Dockerfile) |
| [spryker/php:7.4-alpine3.12](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.12)  | 7.4.8 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.12.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.12 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/7.4/Dockerfile) |
| [spryker/php:7.3-alpine3.12](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.12)  | 7.3.20 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.12.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.12 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/7.3/Dockerfile) |
| [spryker/php:7.2-alpine3.12](https://hub.docker.com/r/spryker/php/tags?name=7.2-alpine3.12)  | 7.2.32 | Alpine 3.12 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2-alpine3.12.svg)](https://microbadger.com/images/spryker/php:7.2-alpine3.12 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.12/7.2/Dockerfile) |
| [spryker/php:7.4-alpine3.11](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.11)  | 7.4.8 | Alpine 3.11 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.11.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.11 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.11/7.4/Dockerfile) |
| [spryker/php:7.3-alpine3.11](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.11)  | 7.3.20 | Alpine 3.11 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.11.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.11 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.11/7.3/Dockerfile) |
| [spryker/php:7.2-alpine3.11](https://hub.docker.com/r/spryker/php/tags?name=7.2-alpine3.11)  | 7.2.32 | Alpine 3.11 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2-alpine3.11.svg)](https://microbadger.com/images/spryker/php:7.2-alpine3.11 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.11/7.2/Dockerfile) |
| [spryker/php:7.4-alpine3.10](https://hub.docker.com/r/spryker/php/tags?name=7.4-alpine3.10)  | 7.4.6 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine3.10.svg)](https://microbadger.com/images/spryker/php:7.4-alpine3.10 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.4/Dockerfile) |
| [spryker/php:7.3-alpine3.10](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.10)  | 7.3.18 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.10.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.10 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:7.2-alpine3.10](https://hub.docker.com/r/spryker/php/tags?name=7.2-alpine3.10)  | 7.2.31 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2-alpine3.10.svg)](https://microbadger.com/images/spryker/php:7.2-alpine3.10 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.2/Dockerfile) |
| [spryker/php:7.3-alpine3.9](https://hub.docker.com/r/spryker/php/tags?name=7.3-alpine3.9)  | 7.3.13 | Alpine 3.9 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine3.9.svg)](https://microbadger.com/images/spryker/php:7.3-alpine3.9 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.9/7.3/Dockerfile) |
| [spryker/php:7.2-alpine3.9](https://hub.docker.com/r/spryker/php/tags?name=7.2-alpine3.9)  | 7.2.26 | Alpine 3.9 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2-alpine3.9.svg)](https://microbadger.com/images/spryker/php:7.2-alpine3.9 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.9/7.2/Dockerfile) |
| [spryker/php:7.4-debian](https://hub.docker.com/r/spryker/php/tags?name=7.4-debian)  | 7.4.8 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.4/Dockerfile) |
| [spryker/php:7.3-debian](https://hub.docker.com/r/spryker/php/tags?name=7.3-debian)  | 7.3.20 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.3-debian.svg)](https://microbadger.com/images/spryker/php:7.3-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.3/Dockerfile) |
| [spryker/php:7.2-debian](https://hub.docker.com/r/spryker/php/tags?name=7.2-debian)  | 7.2.32 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.2-debian.svg)](https://microbadger.com/images/spryker/php:7.2-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.2/Dockerfile) |
| [spryker/php:7.4-debian-buster](https://hub.docker.com/r/spryker/php/tags?name=7.4-debian-buster)  | 7.4.8 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.4/Dockerfile) |
| [spryker/php:7.3-debian-buster](https://hub.docker.com/r/spryker/php/tags?name=7.3-debian-buster)  | 7.3.20 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.3-debian.svg)](https://microbadger.com/images/spryker/php:7.3-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.3/Dockerfile) |
| [spryker/php:7.2-debian-buster](https://hub.docker.com/r/spryker/php/tags?name=7.2-debian-buster)  | 7.2.32 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.2-debian.svg)](https://microbadger.com/images/spryker/php:7.2-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.2/Dockerfile) |

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
 [ ] blackfire 1.36.0
 [ ] newrelic 9.12.0.268
 [ ] tideways 5.1.18

Installed packages, channel pecl.php.net:
=========================================
Package version state
apcu    5.1.18  stable
redis   5.3.1   stable
xdebug  2.9.6   stable
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
EOF
```

## More information
* [Spryker documentation](https://documentation.spryker.com)
* [PHP supported versions](http://php.net/supported-versions.php)
* [PHP official images](https://github.com/docker-library/php)
