from docker_php.dto.distro.distro_transfer import DistroTransfer
from docker_php.dto.php.php_transfer import PhpTransfer
from typing_extensions import Self

from docker_php.dto.third_party_package_transfer import ThirdPartyPackageTransfer


class DockerfileTransfer:
    __distro_transfer: DistroTransfer
    __php_transfer: PhpTransfer
    __third_party_package_transfer: ThirdPartyPackageTransfer

    def __init__(self, distro_transfer: DistroTransfer, php_transfer: PhpTransfer, third_party_package_transfer: ThirdPartyPackageTransfer):
        self.__php_transfer = php_transfer
        self.__distro_transfer = distro_transfer
        self.__third_party_package_transfer = third_party_package_transfer

    def get_distro_transfer(self):
        return self.__distro_transfer

    def set_distro_transfer(self, distro_transfer: DistroTransfer) -> Self:
        self.__distro_transfer = distro_transfer

        return self

    def get_php_transfer(self):
        return self.__php_transfer

    def set_php_transfer(self, php_transfer: PhpTransfer) -> Self:
        self.__php_transfer = php_transfer

        return self

    def get_third_party_package_transfer(self):
        return self.__third_party_package_transfer

    def set_third_party_package_transfer(self, third_party_package_transfer: ThirdPartyPackageTransfer) -> Self:
        self.__third_party_package_transfer = third_party_package_transfer

        return self
