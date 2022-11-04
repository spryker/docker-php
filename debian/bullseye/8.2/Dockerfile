# syntax = docker/dockerfile:1.0.2-experimental
ARG SPRYKER_PHP_VERSION=8.2.0RC3

FROM php:${SPRYKER_PHP_VERSION}-fpm-bullseye

ARG TARGETPLATFORM
ARG COMPOSER_VERSION=2.3.10

ENV srcRoot /data

RUN mkdir -p ${srcRoot}

ARG PHP_RUN_DEPS="\
    libbz2-1.0 \
    libfreetype6 \
    libgmp10 \
    libicu67 \
    libjpeg62-turbo \
    libpng16-16 \
    libwebp6 \
    libxml2 \
    libxpm4 \
    libxslt1.1 \
    libzip4"


ARG PHP_BUILD_DEPS="\
    autoconf \
    libbz2-dev \
    libfreetype6-dev \
    libgmp-dev \
    libicu-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libpq-dev \
    libwebp-dev \
    libxml2-dev \
    libxpm-dev \
    libzip-dev"

ARG PHP_EXTENSIONS="\
    bcmath \
    bz2 \
    gd \
    gmp \
    intl \
    mysqli \
    opcache \
    pcntl \
    pdo_mysql \
    pdo_pgsql \
    pgsql \
    soap \
    sockets \
    zip"

ARG PHP_PECL_EXTENSIONS="\
    apcu \
    redis"

ARG CFLAGS="-I/usr/src/php"
RUN apt update -y \
    && apt install -y \
    bash \
    curl \
    default-mysql-client \
    g++ \
    git \
    gnupg2 \
    graphviz \
    locales-all \
    make \
    netcat-openbsd \
    openssh-client \
    postgresql-client \
    procps \
    python3 \
    unzip \
    wget \
    ${PHP_RUN_DEPS} \
    && \
    apt install -y ${PHP_BUILD_DEPS} \
    && rm -rf /var/lib/apt/lists/ \
    && \
    docker-php-ext-configure gd \
      --disable-gd-jis-conv \
      --with-freetype=/usr \
      --with-jpeg=/usr \
      --with-webp=/usr \
      --with-xpm=/usr \
    && docker-php-ext-install -j5 ${PHP_EXTENSIONS} \
    && \
    pecl install -o -f ${PHP_PECL_EXTENSIONS} xdebug-3.2.0RC1 \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable ${PHP_EXTENSIONS} redis \
    && apt remove -y $PHP_BUILD_DEPS \
    && apt clean

SHELL ["/bin/bash", "-c"]

# Opcache
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
COPY context/php/conf.d/90-opcache.ini /usr/local/etc/php/conf.d/
COPY context/php/conf.d/92-session.ini /usr/local/etc/php/conf.d/
COPY context/php/disabled /usr/local/etc/php/disabled

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION}

# Create application user 'spryker'
RUN addgroup spryker && \
    useradd --home /home/spryker --shell /bin/sh --groups www-data --gid spryker spryker && \
    mkdir -p /home/spryker && \
    chown spryker:spryker /home/spryker && \
    chown spryker:spryker ${srcRoot}

WORKDIR /data

USER spryker
ENV COMPOSER_MEMORY_LIMIT=-1
RUN mkdir -p /home/spryker/.composer
RUN bash -c '[[ $COMPOSER_VERSION == "1"* ]] && composer global require hirak/prestissimo && rm -rf /home/spryker/.composer/cache || true'

USER root
