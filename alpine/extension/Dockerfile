# GRPC + Protobuf extension
ARG MAJOR_PHP_VERSION=8.3
ARG ALPINE_VERSION=3.20
FROM php:${MAJOR_PHP_VERSION}-fpm-alpine${ALPINE_VERSION}

# Set environment variables
ENV srcRoot /data
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so

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
    libzip \
    protobuf \
    grpc"

ARG PHP_BUILD_DEPS="\
    autoconf \
    bzip2-dev \
    freetype-dev \
    gmp-dev \
    icu-dev \
    icu-data-full \
    libjpeg-turbo-dev \
    libpng-dev \
    libwebp-dev \
    libxml2-dev \
    libxpm-dev \
    libzip-dev \
    postgresql-dev \
    rabbitmq-c-dev \
    protobuf-dev \
    grpc-dev \
    g++"

ARG PHP_PECL_EXTENSIONS="\
    opentelemetry \
    protobuf \
    grpc"

ARG ADDITIONAL_PHP_PECL_EXTENSIONS=""

RUN apk add --no-cache \
    bash \
    coreutils \
    curl \
    git \
    make \
    mysql-client \
    netcat-openbsd \
    openssh \
    postgresql-client \
    procps \
    python3 \
    shadow \
    unzip \
    linux-headers \
    libstdc++ \
    ${PHP_RUN_DEPS} \
    && apk add --no-cache --virtual .php-build-deps ${PHP_BUILD_DEPS} \
    && MAKEFLAGS="-j$(nproc)" pecl install -o -f ${PHP_PECL_EXTENSIONS} ${ADDITIONAL_PHP_PECL_EXTENSIONS} \
    && docker-php-ext-enable ${PHP_PECL_EXTENSIONS} \
    && rm -rf /tmp/pear \
    && apk del --no-cache .php-build-deps

RUN mkdir -p ${srcRoot}

# Set environment variables
ENV srcRoot /data
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so

WORKDIR ${srcRoot}

USER root