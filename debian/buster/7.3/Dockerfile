# syntax = docker/dockerfile:1.0.2-experimental
ARG SPRYKER_PHP_VERSION=7.3.15

FROM php:${SPRYKER_PHP_VERSION}-fpm-buster

ENV srcRoot /data

RUN mkdir -p ${srcRoot}

ARG PHP_RUN_DEPS="\
    libicu63 \
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


ARG CFLAGS="-I/usr/src/php"
RUN apt-get update \
    && apt-get install -y \
    bash \
    curl \
    git \
    unzip \
    graphviz \
    netcat-openbsd \
    default-mysql-client \
    openssh-client \
    postgresql-client \
    procps \
    ${PHP_RUN_DEPS} \
    && \
    apt-get install -y ${PHP_BUILD_DEPS} \
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
    && apt-get remove -y $PHP_BUILD_DEPS \
    && apt-get clean

ARG BLACKFIRE_AGENT_SOCKET
ENV BLACKFIRE_AGENT_SOCKET=${BLACKFIRE_AGENT_SOCKET:-'tcp://blackfire:8707'}

# Blackfire
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \
    && curl -A "Docker" -o /tmp/blackfire.so -D - -L -s https://packages.blackfire.io/binaries/blackfire-php/1.31.0/blackfire-php-linux_amd64-php-$version.so \
    && mv /tmp/blackfire.so $(php -r "echo ini_get ('extension_dir');")/blackfire.so

# New Relic
ENV NEWRELIC_ENABLED=0
ENV NEWRELIC_LICENSE=''
ENV NEWRELIC_APPNAME='Spryker'
RUN curl -L 'https://download.newrelic.com/php_agent/archive/9.7.0.258/newrelic-php5-9.7.0.258-linux-musl.tar.gz' | tar -C /tmp -zx \
  && export NR_INSTALL_USE_CP_NOT_LN=1 \
  && export NR_INSTALL_SILENT=1 \
  && /tmp/newrelic-php5-*/newrelic-install install \
  && rm -rf /tmp/newrelic-php5-* /tmp/nrinstall* \
  && /usr/bin/install -d -m 777 /var/log/newrelic/ \
  && rm /usr/local/etc/php/conf.d/newrelic.ini \
  && ln -s /lib64/ld-linux-x86-64.so.2 /lib/ld-linux-x86-64.so.2

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
COPY context/php/conf.d/opcache.ini /usr/local/etc/php/conf.d/
COPY context/php/disabled /usr/local/etc/php/disabled

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Create application user 'spryker'
RUN addgroup spryker && \
    useradd --home /home/spryker --shell /bin/sh --groups www-data --gid spryker spryker && \
    mkdir -p /home/spryker && \
    chown spryker:spryker /home/spryker && \
    chown spryker:spryker ${srcRoot}

WORKDIR /data

USER spryker
ENV COMPOSER_MEMORY_LIMIT=-1
RUN mkdir -p /home/spryker/.composer && \
    composer global require hirak/prestissimo && \
    rm -rf /home/spryker/.composer/cache

USER root
