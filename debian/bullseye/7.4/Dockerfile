# syntax = docker/dockerfile:1.0.2-experimental
ARG SPRYKER_PHP_VERSION=7.4.22

FROM php:${SPRYKER_PHP_VERSION}-fpm-bullseye

ARG COMPOSER_VERSION=2.0.12
ARG BLACKFIRE_VERSION=1.57.0
ARG NEWRELIC_VERSION=9.16.0.295
ARG TIDEWAYS_VERSION=latest

ENV srcRoot /data

RUN mkdir -p ${srcRoot}

ARG PHP_RUN_DEPS="\
    libicu67 \
    libbz2-1.0 \
    libxslt1.1 \
    libpng16-16 \
    libfreetype6 \
    libxpm4 \
    libwebp6 \
    libxml2 \
    libjpeg62-turbo \
    libzip4 \
    libgmp10"


ARG PHP_BUILD_DEPS="\
    libpq-dev \
    libpng-dev \
    libwebp-dev \
    libjpeg62-turbo-dev \
    libxpm-dev \
    libxml2-dev \
    libfreetype6-dev \
    libgmp-dev \
    libicu-dev \
    libbz2-dev \
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

ARG PHP_PECL_EXTENSIONS="\
    apcu \
    redis"

ARG CFLAGS="-I/usr/src/php"
RUN apt update -y \
    && apt install -y \
    bash \
    curl \
    git \
    gnupg2 \
    unzip \
    graphviz \
    netcat-openbsd \
    default-mysql-client \
    openssh-client \
    postgresql-client \
    supervisor \
    procps \
    locales-all \
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
    pecl install -o -f ${PHP_PECL_EXTENSIONS} xdebug \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable ${PHP_EXTENSIONS} redis \
    && apt remove -y $PHP_BUILD_DEPS \
    && apt clean

# Blackfire
ENV BLACKFIRE_AGENT_SOCKET=''
RUN version=$(php -r "echo PHP_MAJOR_VERSION . PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire.so -D - -L -s https://packages.blackfire.io/binaries/blackfire-php/${BLACKFIRE_VERSION}/blackfire-php-linux_amd64-php-$version.so \
    && mv /tmp/blackfire.so $(php -r "echo ini_get ('extension_dir');")/blackfire.so

# New Relic
ENV NEWRELIC_ENABLED=0
ENV NEWRELIC_LICENSE=''
ENV NEWRELIC_APPNAME='Spryker'
RUN curl -L "https://download.newrelic.com/php_agent/archive/${NEWRELIC_VERSION}/newrelic-php5-${NEWRELIC_VERSION}-linux.tar.gz" | tar -C /tmp -zx \
  && export NR_INSTALL_USE_CP_NOT_LN=1 \
  && export NR_INSTALL_SILENT=1 \
  && /tmp/newrelic-php5-*/newrelic-install install \
  && rm -rf /tmp/newrelic-php5-* /tmp/nrinstall* \
  && /usr/bin/install -d -m 777 /var/log/newrelic/ \
  && rm /usr/local/etc/php/conf.d/newrelic.ini \
  && ln -s /lib64/ld-linux-x86-64.so.2 /lib/ld-linux-x86-64.so.2

# Tideways
RUN echo 'deb http://s3-eu-west-1.amazonaws.com/tideways/packages debian main' > /etc/apt/sources.list.d/tideways.list && \
    curl -sS 'https://s3-eu-west-1.amazonaws.com/tideways/packages/EEB5E8F4.gpg' | apt-key add - && \
    apt update -y && \
    DEBIAN_FRONTEND=noninteractive apt -yq install tideways-php && \
    apt autoremove --assume-yes && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

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
