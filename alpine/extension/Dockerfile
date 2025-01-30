## GRPC + Protobuf extension
#ARG MAJOR_PHP_VERSION=8.3
#ARG ALPINE_VERSION=3.20
#FROM php:${MAJOR_PHP_VERSION}-fpm-alpine${ALPINE_VERSION}
#
## Set environment variables
#ENV srcRoot /data
#ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so
#
#ARG PHP_RUN_DEPS="\
#    freetype \
#    gmp \
#    gnu-libiconv \
#    icu-libs \
#    libbz2 \
#    libc6-compat \
#    libjpeg-turbo \
#    libpng \
#    libwebp \
#    libxml2 \
#    libxpm \
#    libxslt \
#    libzip \
#    protobuf \
#    grpc"
#
#ARG PHP_BUILD_DEPS="\
#    autoconf \
#    bzip2-dev \
#    freetype-dev \
#    gmp-dev \
#    icu-dev \
#    icu-data-full \
#    libjpeg-turbo-dev \
#    libpng-dev \
#    libwebp-dev \
#    libxml2-dev \
#    libxpm-dev \
#    libzip-dev \
#    postgresql-dev \
#    rabbitmq-c-dev \
#    protobuf-dev \
#    grpc-dev \
#    g++"
#
#ARG PHP_PECL_EXTENSIONS="\
#    opentelemetry \
#    protobuf \
#    grpc"
#
#ARG ADDITIONAL_PHP_PECL_EXTENSIONS=""
#
#RUN apk add --no-cache \
#    bash \
#    coreutils \
#    curl \
#    git \
#    make \
#    mysql-client \
#    netcat-openbsd \
#    openssh \
#    postgresql-client \
#    procps \
#    python3 \
#    shadow \
#    unzip \
#    linux-headers \
#    libstdc++ \
#    ${PHP_RUN_DEPS} \
#    && apk add --no-cache --virtual .php-build-deps ${PHP_BUILD_DEPS} \
#    && MAKEFLAGS="-j$(nproc)" pecl install -o -f ${PHP_PECL_EXTENSIONS} ${ADDITIONAL_PHP_PECL_EXTENSIONS} \
#    && docker-php-ext-enable ${PHP_PECL_EXTENSIONS} \
#    && rm -rf /tmp/pear \
#    && apk del --no-cache .php-build-deps
#
#RUN mkdir -p ${srcRoot}
#
## Set environment variables
#ENV srcRoot /data
#ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so
#
#WORKDIR ${srcRoot}
#
#USER root

#ARG MAJOR_PHP_VERSION=8.3
#ARG ALPINE_VERSION=3.20
#FROM php:${MAJOR_PHP_VERSION}-fpm-alpine${ALPINE_VERSION}
#
## Install required dependencies
#RUN apk add --no-cache \
#    php83-pear \
#    php83-dev \
#    autoconf \
#    g++ \
#    libtool \
#    make \
#    linux-headers \
#    grpc grpc-dev protobuf protobuf-dev \
#    && pecl install grpc --configure-options="--disable-debug --enable-optimize" \
#    && docker-php-ext-enable grpc \
#    && apk del --no-cache php-dev autoconf g++ libtool make linux-headers grpc-dev protobuf-dev \
#    && rm -rf /tmp/pear
#
#RUN apk add --no-cache strip
#RUN strip --strip-unneeded /usr/local/lib/php/extensions/no-debug-non-zts-20230831/grpc.so
#
## Verify GRPC installation
#RUN php --ri grpc || echo "GRPC INSTALLATION FAILED!"


#ARG MAJOR_PHP_VERSION=8.3
#ARG ALPINE_VERSION=3.20
#FROM php:${MAJOR_PHP_VERSION}-fpm-alpine${ALPINE_VERSION}
#
## Install GRPC and Protobuf extensions
#RUN apk add --no-cache php83-pecl-grpc php83-pecl-protobuf
#
## Manually enable GRPC and Protobuf (since `docker-php-ext-enable` does not work)
#RUN echo "extension=grpc.so" > /etc/php83/conf.d/00_grpc.ini \
#    && echo "extension=protobuf.so" > /etc/php83/conf.d/00_protobuf.ini
#
## Verify installation
#RUN php --ri grpc || echo "GRPC INSTALLATION FAILED!"
#RUN php --ri protobuf || echo "PROTOBUF INSTALLATION FAILED!"

#ARG MAJOR_PHP_VERSION=8.3
#ARG ALPINE_VERSION=3.20
#FROM php:${MAJOR_PHP_VERSION}-fpm-alpine${ALPINE_VERSION}
#
## Install GRPC extension
#RUN apk add --no-cache php83-pecl-grpc
#
## Manually enable GRPC
#RUN echo "extension=grpc.so" > /etc/php83/conf.d/00_grpc.ini
#
## Verify GRPC installation
#RUN php --ri grpc || echo "GRPC INSTALLATION FAILED!"

ARG MAJOR_PHP_VERSION=8.3
ARG ALPINE_VERSION=3.20
FROM php:${MAJOR_PHP_VERSION}-fpm-alpine${ALPINE_VERSION}

# Add community repository where PHP extensions are available
RUN echo "https://dl-cdn.alpinelinux.org/alpine/v$(cut -d'.' -f1,2 /etc/alpine-release)/community" >> /etc/apk/repositories

RUN apk add --no-cache \
    php83-pecl-grpc \
    php83-pecl-protobuf

RUN ln -s /usr/lib/php83/modules/grpc.so /usr/local/lib/php/extensions/no-debug-non-zts-20230831/grpc.so && \
    ln -s /usr/lib/php83/modules/protobuf.so /usr/local/lib/php/extensions/no-debug-non-zts-20230831/protobuf.so

RUN echo "extension=grpc.so" > /usr/local/etc/php/conf.d/docker-php-ext-grpc.ini && \
    echo "extension=protobuf.so" > /usr/local/etc/php/conf.d/docker-php-ext-protobuf.ini

# Verify GRPC installation
RUN php -m | grep grpc