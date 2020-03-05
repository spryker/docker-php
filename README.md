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
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags) | 7.3.15 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:latest.svg)](https://microbadger.com/images/spryker/php:latest "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:7.4](https://hub.docker.com/r/spryker/php/tags)  | 7.4.3 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4.svg)](https://microbadger.com/images/spryker/php:7.4 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.4/Dockerfile) |
| [spryker/php:7.3](https://hub.docker.com/r/spryker/php/tags)  | 7.3.15 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3.svg)](https://microbadger.com/images/spryker/php:7.3 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:7.2](https://hub.docker.com/r/spryker/php/tags)  | 7.2.28 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2.svg)](https://microbadger.com/images/spryker/php:7.2 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.2/Dockerfile) |
| [spryker/php:7.4-alpine3.10](https://hub.docker.com/r/spryker/php/tags)  | 7.4.3 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-alpine.svg)](https://microbadger.com/images/spryker/php:7.4-alpine "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.4/Dockerfile) |
| [spryker/php:7.3-alpine3.10](https://hub.docker.com/r/spryker/php/tags)  | 7.3.15 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine.svg)](https://microbadger.com/images/spryker/php:7.3-alpine "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.3/Dockerfile) |
| [spryker/php:7.2-alpine3.10](https://hub.docker.com/r/spryker/php/tags)  | 7.2.28 | Alpine 3.10 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2-alpine.svg)](https://microbadger.com/images/spryker/php:7.2-alpine "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.10/7.2/Dockerfile) |
| [spryker/php:7.3-alpine3.9](https://hub.docker.com/r/spryker/php/tags)  | 7.3.13 | Alpine 3.9 |[![](https://images.microbadger.com/badges/image/spryker/php:7.3-alpine.svg)](https://microbadger.com/images/spryker/php:7.3-alpine "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.9/7.3/Dockerfile) |
| [spryker/php:7.2-alpine3.9](https://hub.docker.com/r/spryker/php/tags)  | 7.2.26 | Alpine 3.9 |[![](https://images.microbadger.com/badges/image/spryker/php:7.2-alpine.svg)](https://microbadger.com/images/spryker/php:7.2-alpine "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/alpine/3.9/7.2/Dockerfile) |
| [spryker/php:7.4-debian](https://hub.docker.com/r/spryker/php/tags)  | 7.4.3 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.4/Dockerfile) |
| [spryker/php:7.3-debian](https://hub.docker.com/r/spryker/php/tags)  | 7.3.15 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.3-debian.svg)](https://microbadger.com/images/spryker/php:7.3-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.3/Dockerfile) |
| [spryker/php:7.2-debian](https://hub.docker.com/r/spryker/php/tags)  | 7.2.28 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.2-debian.svg)](https://microbadger.com/images/spryker/php:7.2-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.2/Dockerfile) |
| [spryker/php:7.4-debian-buster](https://hub.docker.com/r/spryker/php/tags)  | 7.4.3 | Debian "buster" |[![](https://images.microbadger.com/badges/image/spryker/php:7.4-debian.svg)](https://microbadger.com/images/spryker/php:7.4-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.4/Dockerfile) |
| [spryker/php:7.3-debian-buster](https://hub.docker.com/r/spryker/php/tags)  | 7.3.15 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.3-debian.svg)](https://microbadger.com/images/spryker/php:7.3-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.3/Dockerfile) |
| [spryker/php:7.2-debian-buster](https://hub.docker.com/r/spryker/php/tags)  | 7.2.28 | Debian "buster"| [![](https://images.microbadger.com/badges/image/spryker/php:7.2-debian.svg)](https://microbadger.com/images/spryker/php:7.2-debian "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/debian/7.2/Dockerfile) |


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
FROM spryker/php:7.3
```

### docker-compose.yml
```yaml
service1:
    image: spryker/php:7.2-debian
```

## PHP extensions

```
INSTALLED EXTENSIONS
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

INSTALLED PACKAGES, CHANNEL PECL.PHP.NET:
=========================================
PACKAGE VERSION STATE
redis   5.1.1   stable
xdebug  2.9.2   stable
```
##### Run the following to get the report
```bash
$ docker run -i --rm spryker/php:latest bash -s<<'EOF'
    docker-php-source extract
    echo "INSTALLED EXTENSIONS";
    echo "====================";
    for ext in `ls /usr/src/php/ext`; do echo ' ' `php -r "if (extension_loaded('$ext' !== 'opcache' ? '$ext' : 'Zend OPcache')) { echo '[x] $ext'; } else { echo '[ ] $ext'; }"`; done
    echo "";
    pear list -c pecl
EOF
```

## More information
* [Spryker documentation](https://documentation.spryker.com)
* [PHP supported versions](http://php.net/supported-versions.php)
* [PHP official images](https://github.com/docker-library/php)
