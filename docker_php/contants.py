import os

PACKAGE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

CONFIG_PATH = PACKAGE_ROOT_PATH + os.sep + '..' + os.sep + 'config' + os.sep
BUILD_PATH = PACKAGE_ROOT_PATH + os.sep + '..' + os.sep + 'build' + os.sep
DOCKERHUB_PHP_URL = 'https://hub.docker.com/v2/repositories/library/php/tags'

PHP_LAST_MAJOR_VERSION = 8
CONFIG_PHP_KEY_NAME = 'php'
CONFIG_PHP_TAG_FORMAT_KEY_NAME = 'php-tag-format'
