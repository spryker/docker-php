from typing_extensions import Self


class PhpVersionTransfer:
    __php_version: str
    __major: int
    __minor: int
    __patch: int

    def __init__(self, php_version: str):
        self.__php_version = php_version
        self.__major, self.__minor, self.__patch = php_version.split('.')

    def get_version(self) -> str:
        return self.__php_version

    def set_version(self, php_version: str) -> Self:
        self.__php_version = php_version
        self.__major, self.__minor, self.__patch = php_version.split('.')

        return self

    def get_major_version(self) -> int:
        return self.__major

    def get_minor_version(self) -> int:
        return self.__minor

    def get_patch_version(self) -> int:
        return self.__patch

