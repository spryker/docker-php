# PHP-FPM

[![Docker Stars](https://img.shields.io/docker/stars/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![Docker Pulls](https://img.shields.io/docker/pulls/spryker/php.svg)](https://store.docker.com/community/images/spryker/php)
[![microbadger version](https://images.microbadger.com/badges/version/spryker/php.svg)](https://microbadger.com/images/spryker/php "Get your own version badge on microbadger.com")
[![microbadger image](https://images.microbadger.com/badges/image/spryker/php.svg)](https://microbadger.com/images/spryker/php "Get your own image badge on microbadger.com")

# Description

Extends official PHP Docker images with extensions and tools to be able to run Spryker on.

* Based on: Official PHP images and `Alpine 3.9`
* Users: `root`, `spryker`
* Working directory: `/data`
* Includes:
  * [PHP extensions](#php-extensions)
  * PostgreSQL client
  * MySQL client
  * CURL
  * OpenSSH
  * Composer
  * `hirak/prestissimo`

> Note: Provided images require additional configuration for development, staging and production use.

## Tags

| Tag     | PHP version     | Details     | Dockerfile     |
| :------------- | :------------- | :------------- | :------------- |
| [spryker/php:latest](https://hub.docker.com/r/spryker/php/tags) | 7.2.17 | [![](https://images.microbadger.com/badges/image/spryker/php:latest.svg)](https://microbadger.com/images/spryker/php:latest "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/7.2/Dockerfile) |
| [spryker/php:7.3](https://hub.docker.com/r/spryker/php/tags)  | 7.3.4 | [![](https://images.microbadger.com/badges/image/spryker/php:7.3.svg)](https://microbadger.com/images/spryker/php:7.3 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/7.3/Dockerfile) |
| [spryker/php:7.2](https://hub.docker.com/r/spryker/php/tags)  | 7.2.17 | [![](https://images.microbadger.com/badges/image/spryker/php:7.2.svg)](https://microbadger.com/images/spryker/php:7.2 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/7.2/Dockerfile) |
| [spryker/php:7.1](https://hub.docker.com/r/spryker/php/tags)  | 7.1.28 | [![](https://images.microbadger.com/badges/image/spryker/php:7.1.svg)](https://microbadger.com/images/spryker/php:7.1 "Get your own image badge on microbadger.com") | [:link:](https://github.com/spryker/docker-php/blob/master/7.1/Dockerfile) |


## How to use

### Pull image
```bash
$ docker pull spryker/php
$ docker pull spryker/php:7.3
```

### Run container
```bash
$ docker run -i --rm spryker/php:latest php -v
```

### Dockerfile
```dockerfile
FROM spryker/php:7.2
```

### docker-compose.yml
```yaml
service1:
    image: spryker/php:7.1
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

Installed packages, channel pecl.php.net:
=========================================
Package Version State
decimal 1.3.0   stable
redis   5.0.2   stable
xdebug  2.7.2   stable
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
