# syntax = docker/dockerfile:1.0.2-experimental
ARG SPRYKER_PHP_VERSION=8.0.21

FROM php:${SPRYKER_PHP_VERSION}-fpm-bullseye

ARG TARGETPLATFORM
ARG COMPOSER_VERSION=2.3.4
ARG BLACKFIRE_VERSION=1.57.0
ARG BLACKFIRE_PHP_VERSION=80
ARG NEWRELIC_VERSION=9.18.1.303
ARG TIDEWAYS_VERSION=5.4.28
ARG TIDEWAYS_PHP_VERSION=8.0

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
    g++ \
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
    git \
    gnupg2 \
    graphviz \
    locales-all \
    make \
    netcat-openbsd \
    openssh-client \
    postgresql-client \
    procps \
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
    pecl install -o -f ${PHP_PECL_EXTENSIONS} xdebug \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable ${PHP_EXTENSIONS} redis \
    && apt remove -y $PHP_BUILD_DEPS \
    && apt clean

# Blackfire
ENV BLACKFIRE_AGENT_SOCKET=''
RUN architecture=$(case ${TARGETPLATFORM} in "linux/amd64") echo "amd64" ;; linux/arm64) echo "arm64" ;; *) echo "amd64" ;; esac) \
    && curl -A "Docker" -o /tmp/blackfire.so -D - -L -s https://packages.blackfire.io/binaries/blackfire-php/${BLACKFIRE_VERSION}/blackfire-php-linux_${architecture}-php-${BLACKFIRE_PHP_VERSION}.so \
    && mv /tmp/blackfire.so $(php -r "echo ini_get ('extension_dir');")/blackfire.so

# NewRelic release for PHP8 in progress

# New Relic
ENV NEWRELIC_ENABLED=0
ENV NEWRELIC_LICENSE=''
ENV NEWRELIC_APPNAME='Spryker'
ENV NEWRELIC_DISTRIBUTED_TRACING_ENABLED=0
ENV NEWRELIC_TRANSACTION_TRACER_ENABLED=0
ENV NEWRELIC_SPAN_EVENTS_ENABLED=0
ENV NEWRELIC_TRANSACTION_TRACER_THRESHOLD=0
ENV NEWRELIC_DISTRIBUTED_TRACING_EXCLUDE_NEWRELIC_HEADER=0
RUN curl -L "https://download.newrelic.com/php_agent/archive/${NEWRELIC_VERSION}/newrelic-php5-${NEWRELIC_VERSION}-linux.tar.gz" | tar -C /tmp -zx \
  && export NR_INSTALL_USE_CP_NOT_LN=1 \
  && export NR_INSTALL_SILENT=1 \
  && /tmp/newrelic-php5-*/newrelic-install install \
  && rm -rf /tmp/newrelic-php5-* /tmp/nrinstall* \
  && /usr/bin/install -d -m 777 /var/log/newrelic/ \
  && rm /usr/local/etc/php/conf.d/newrelic.ini \
  && ln -s /lib64/ld-linux-x86-64.so.2 /lib/ld-linux-x86-64.so.2

# Tideways
RUN bash -c 'if [ "${TARGETPLATFORM}" == "linux/amd64" ]; then echo "deb http://s3-eu-west-1.amazonaws.com/tideways/packages debian main" > /etc/apt/sources.list.d/tideways.list && \
   curl -sS "https://s3-eu-west-1.amazonaws.com/tideways/packages/EEB5E8F4.gpg" | apt-key add - && \
   apt update -y && \
   DEBIAN_FRONTEND=noninteractive apt -yq install tideways-php && \
   apt autoremove --assume-yes && \
   apt clean && \
   rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; fi'

RUN bash -c 'if [ "${TARGETPLATFORM}" == "linux/arm64" ]; then \
    wget "https://s3-eu-west-1.amazonaws.com/tideways/extension/${TIDEWAYS_VERSION}/tideways-php-${TIDEWAYS_VERSION}-arm64.tar.gz" && \
    tar xvzf tideways-php-${TIDEWAYS_VERSION}-arm64.tar.gz && \
    cp ./tideways-${TIDEWAYS_VERSION}/tideways-php-${TIDEWAYS_PHP_VERSION}.so $(php-config --extension-dir)/tideways.so; fi' \

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
