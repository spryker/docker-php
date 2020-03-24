# syntax = docker/dockerfile:1.0.2-experimental
ARG SPRYKER_PHP_VERSION=7.3.15

FROM php:${SPRYKER_PHP_VERSION}-fpm-alpine3.10

ENV srcRoot /data

RUN mkdir -p ${srcRoot}

ARG PHP_RUN_DEPS="\
    icu-libs \
    libbz2 \
    libxslt \
    libpng \
    freetype \
    libxpm \
    libwebp \
    libxml2 \
    libjpeg-turbo \
    libzip \
    gmp"


ARG PHP_BUILD_DEPS="\
    postgresql-dev \
    libpng-dev \
    libwebp-dev \
    libjpeg-turbo-dev \
    libxpm-dev \
    libxml2-dev \
    freetype-dev \
    gmp-dev \
    icu-dev \
    bzip2-dev \
    libzip-dev \
    autoconf \
    g++ \
    make"

ARG PHP_EXTENSIONS="\
    gd \
    gmp \
    intl \
    pdo_pgsql \
    pdo_mysql \
    mysqli \
    pgsql \
    bcmath \
    bz2 \
    sockets \
    soap \
    pcntl \
    opcache \
    zip"


ARG CFLAGS="-I/usr/src/php"
RUN apk update \
    && apk add --no-cache \
    bash \
    curl \
    git \
    unzip \
    graphviz \
    netcat-openbsd \
    mysql-client \
    openssh \
    postgresql-client \
    procps \
    shadow \
    coreutils \
    ${PHP_RUN_DEPS} \
    && \
    apk add --no-cache --virtual .php-build-deps ${PHP_BUILD_DEPS} \
    && rm -rf /var/lib/apt/lists/ \
    && \
    docker-php-ext-configure gd \
      --disable-gd-jis-conv \
      --with-freetype-dir=/usr \
      --with-jpeg-dir=/usr \
      --with-png-dir=/usr \
      --with-webp-dir=/usr \
      --with-xpm-dir=/usr \
    && docker-php-ext-install -j5 ${PHP_EXTENSIONS} \
    && \
    pecl install -o -f redis xdebug \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable ${PHP_EXTENSIONS} redis \
    && apk del --no-cache .php-build-deps \
    # Related to https://github.com/docker-library/php/issues/240
    && apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community gnu-libiconv

ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so

RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire.so -D - -L -s https://packages.blackfire.io/binaries/blackfire-php/1.31.0/blackfire-php-alpine_amd64-php-$version.so \
    && mv /tmp/blackfire.so $(php -r "echo ini_get ('extension_dir');")/blackfire.so

ENV NEWRELIC_ENABLED=0
ENV NEWRELIC_LICENSE=''
ENV NEWRELIC_APPNAME='Spryker'
RUN curl -L 'https://download.newrelic.com/php_agent/release/newrelic-php5-9.7.0.258-linux-musl.tar.gz' | tar -C /tmp -zx && \
  export NR_INSTALL_USE_CP_NOT_LN=1 && \
  export NR_INSTALL_SILENT=1 && \
  /tmp/newrelic-php5-*/newrelic-install install && \
  rm -rf /tmp/newrelic-php5-* /tmp/nrinstall*

RUN /usr/bin/install -d -m 777 /var/run/opcache

# Remove default FPM pool
RUN rm /usr/local/etc/php-fpm.d/www.conf && \
    rm /usr/local/etc/php-fpm.d/docker.conf && \
    rm /usr/local/etc/php-fpm.d/zz-docker.conf

# Add FPM configs
COPY context/php/php-fpm.d/worker.conf /usr/local/etc/php-fpm.d/worker.conf
COPY context/php/php-fpm.conf  /usr/local/etc/php-fpm.conf

# Copy php.ini configuration
COPY context/php/php.ini /usr/local/etc/php/
COPY context/php/conf.d/opcache.ini /usr/local/etc/php/conf.d/
COPY context/php/conf.d/blackfire.ini.dist /usr/local/etc/php/conf.d/
COPY context/php/conf.d/newrelic.ini.dist /usr/local/etc/php/conf.d/

WORKDIR /data

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Create application user 'spryker'
RUN addgroup spryker && \
    adduser -h /home/spryker -s /bin/sh -G www-data -D spryker && \
    chown spryker:spryker ${srcRoot}

USER spryker
ENV COMPOSER_MEMORY_LIMIT=-1
RUN mkdir -p /home/spryker/.composer && \
    composer global require hirak/prestissimo && \
    rm -rf /home/spryker/.composer/cache

USER root
