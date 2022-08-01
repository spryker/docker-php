from docker_php.dto.distro.distro_packages_transfer import DistroPackagesTransfer
from typing_extensions import Self


class DistroTransfer:
    __name: str
    __version: str
    __packages: DistroPackagesTransfer

    def __init__(
        self,
        name: str,
        version: str,
        packages: DistroPackagesTransfer
    ):
        self.__name = name
        self.__version = version
        self.__packages = packages

    def get_name(self) -> str:
        return self.__name

    def get_version(self) -> str:
        return self.__version

    def get_packages(self) -> DistroPackagesTransfer:
        return self.__packages

    def set_name(self, name: str) -> Self:
        self.__name = name

        return self

    def set_version(self, version: str) -> Self:
        self.__version = version

        return self

    def set_packages(self, packages: DistroPackagesTransfer) -> Self:
        self.__packages = packages

        return self
