# syntax = docker/dockerfile:experimental
ARG SPRYKER_PHP_VERSION=7.1.27

FROM php:${SPRYKER_PHP_VERSION}-fpm-alpine3.9

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
    libxpm \
    libjpeg-turbo \
    gmp"


ARG PHP_BUILD_DEPS="\
    postgresql-dev \
    libpng-dev \
    libwebp-dev \
    libjpeg-turbo-dev \
    libxpm-dev \
    freetype-dev \
    gmp-dev \
    icu-dev \
    bzip2-dev \
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
    opcache"


ARG CFLAGS="-I/usr/src/php"
RUN apk update \
    && apk add --no-cache \
    shadow \
    procps \
    openssh \
    curl \
    bash \
    git \
    postgresql-client \
    mysql-client \
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
    pecl install -o -f  redis xdebug \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable ${PHP_EXTENSIONS} redis \
    && apk del --no-cache .php-build-deps \
    # Related to https://github.com/docker-library/php/issues/240
    && apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community gnu-libiconv

ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Create a special user 'spryker'
RUN addgroup spryker
RUN adduser -h /home/spryker -s /bin/sh -G www-data -D spryker
RUN chown spryker:spryker ${srcRoot}

# Remove default FPM pool
RUN rm /usr/local/etc/php-fpm.d/www.conf && \
    rm /usr/local/etc/php-fpm.d/docker.conf && \
    rm /usr/local/etc/php-fpm.d/zz-docker.conf

COPY context/php/php-fpm.d/worker.conf /usr/local/etc/php-fpm.d/worker.conf
COPY context/php/php-fpm.conf  /usr/local/etc/php-fpm.conf

# Copy php.ini configuration
COPY context/php/php.ini /usr/local/etc/php/
COPY context/php/conf.d/opcache.ini /usr/local/etc/php/conf.d/

WORKDIR /data

USER spryker

ENV COMPOSER_MEMORY_LIMIT=-1
RUN composer global require hirak/prestissimo aws/aws-sdk-php

USER root
