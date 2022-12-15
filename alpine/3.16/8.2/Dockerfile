# syntax = docker/dockerfile:1.0.2-experimental
ARG SPRYKER_PHP_VERSION=8.2.0

FROM php:${SPRYKER_PHP_VERSION}-fpm-alpine3.16

ARG TARGETPLATFORM
ARG COMPOSER_VERSION=2.4.3
ARG BLACKFIRE_VERSION=1.86.1
ARG BLACKFIRE_PHP_VERSION=82
ARG TIDEWAYS_VERSION=5.5.12
ARG TIDEWAYS_PHP_VERSION=8.2

ENV srcRoot /data

RUN mkdir -p ${srcRoot}

ARG PHP_RUN_DEPS="\
    freetype \
    gmp \
    gnu-libiconv \
    icu-libs \
    libbz2 \
    libc6-compat \
    libjpeg-turbo \
    libpng \
    libwebp \
    libxml2 \
    libxpm \
    libxslt \
    libzip"


ARG PHP_BUILD_DEPS="\
    autoconf \
    bzip2-dev \
    freetype-dev \
    gmp-dev \
    icu-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libwebp-dev \
    libxml2-dev \
    libxpm-dev \
    libzip-dev \
    postgresql-dev"

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
    zip"

ARG PHP_PECL_EXTENSIONS="\
    apcu \
    redis"

ARG ADDITIONAL_PHP_PECL_EXTENSIONS="\
   xdebug-3.2.0 \
   xhprof"

ARG CFLAGS="-I/usr/src/php"
RUN apk update \
    && apk add --no-cache \
    bash \
    coreutils \
    curl \
    g++ \
    git \
    graphviz \
    make \
    mysql-client \
    netcat-openbsd \
    openssh \
    postgresql-client \
    procps \
    python3 \
    shadow \
    unzip \
    ${PHP_RUN_DEPS} \
    && \
    apk add --no-cache --virtual .php-build-deps ${PHP_BUILD_DEPS} \
    && rm -rf /var/lib/apt/lists/ \
    && \
    docker-php-ext-configure gd \
      --disable-gd-jis-conv \
      --with-freetype=/usr \
      --with-jpeg=/usr \
      --with-webp=/usr \
      --with-xpm=/usr \
    && docker-php-ext-install -j5 ${PHP_EXTENSIONS} \
    && apk add --update linux-headers \
    && \
    pecl install -o -f ${PHP_PECL_EXTENSIONS} ${ADDITIONAL_PHP_PECL_EXTENSIONS} \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable ${PHP_EXTENSIONS} ${PHP_PECL_EXTENSIONS} \
    && apk del --no-cache .php-build-deps

RUN curl -sSLf \
        -o /usr/local/bin/install-php-extensions \
        https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions && \
    chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions sockets

# Related to https://github.com/docker-library/php/issues/240
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so

# Blackfire
ENV BLACKFIRE_AGENT_SOCKET=''
RUN architecture=$(case ${TARGETPLATFORM} in "linux/amd64") echo "amd64" ;; linux/arm64) echo "arm64" ;; *) echo "amd64" ;; esac) \
    && curl -A "Docker" -o /tmp/blackfire.so -D - -L -s https://packages.blackfire.io/binaries/blackfire-php/${BLACKFIRE_VERSION}/blackfire-php-alpine_${architecture}-php-${BLACKFIRE_PHP_VERSION}.so \
    && mv /tmp/blackfire.so $(php -r "echo ini_get ('extension_dir');")/blackfire.so

# Tideways
ENV TIDEWAYS_APIKEY=''
ENV TIDEWAYS_DAEMON_URI=''
ENV TIDEWAYS_CLI_ENABLED=0
RUN bash -c 'if [ "${TARGETPLATFORM}" == "linux/amd64" ]; then \
    wget https://s3-eu-west-1.amazonaws.com/tideways/extension/${TIDEWAYS_VERSION}/tideways-php-${TIDEWAYS_VERSION}-alpine.tar.gz \
    && tar xvzf tideways-php-${TIDEWAYS_VERSION}-alpine.tar.gz \
    && cp ./build/dist/tideways-php-alpine-${TIDEWAYS_PHP_VERSION}.so $(php-config --extension-dir)/tideways.so; fi'

RUN bash -c 'if [ "${TARGETPLATFORM}" == "linux/arm64" ]; then \
    wget https://s3-eu-west-1.amazonaws.com/tideways/extension/${TIDEWAYS_VERSION}/tideways-php-${TIDEWAYS_VERSION}-alpine-arm64.tar.gz \
    && tar xvzf tideways-php-${TIDEWAYS_VERSION}-alpine-arm64.tar.gz \
    && cp ./build/dist/tideways-php-alpine-${TIDEWAYS_PHP_VERSION}.so $(php-config --extension-dir)/tideways.so; fi'

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

WORKDIR /data

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION}

# Create application user 'spryker'
RUN addgroup spryker && \
    adduser -h /home/spryker -s /bin/sh -G www-data -D spryker && \
    chown spryker:spryker ${srcRoot}

USER spryker
ENV COMPOSER_MEMORY_LIMIT=-1
RUN mkdir -p /home/spryker/.composer
RUN bash -c '[[ $COMPOSER_VERSION == "1"* ]] && composer global require hirak/prestissimo && rm -rf /home/spryker/.composer/cache || true'

USER root