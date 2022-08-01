from typing_extensions import Self

from docker_php.dto.php.php_version_transfer import PhpVersionTransfer


class PhpTransfer:
    __php_image_tag: str
    __extensions: list
    __pecl_extensions: list
    __version_transfer: PhpVersionTransfer

    def __init__(
        self,
        version_transfer: PhpVersionTransfer,
        php_image_tag: str,
        extensions: list,
        pecl_extensions: list
    ):
        self.__version_transfer = version_transfer
        self.__php_image_tag = php_image_tag
        self.__extensions = extensions
        self.__pecl_extensions = pecl_extensions

    def get_extensions(self):
        return self.__extensions

    def set_extensions(self, extensions: list) -> Self:
        self.__extensions = extensions
        return self

    def get_version_trasfer(self) -> PhpVersionTransfer:
        return self.__version_transfer

    def set_version_transfer(self, version: PhpVersionTransfer) -> Self:
        self.__version_transfer = version

        return self

    def get_pecl_extensions(self):
        return self.__pecl_extensions

    def set_pecl_extensions(self, pecl_extensions: list) -> Self:
        self.__pecl_extensions = pecl_extensions

        return self

    def get_php_image_tag(self):
        return self.__php_image_tag

    def set_php_image_tag(self, php_image_tag: str) -> Self:
        self.__php_image_tag = php_image_tag

        return self
