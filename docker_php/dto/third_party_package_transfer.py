from typing_extensions import Self


class ThirdPartyPackageTransfer:
    __third_party_packages: dict

    def __init__(self, third_party_packages: dict = {}):
        self.__third_party_packages = third_party_packages

    def get_third_party_packages(self):
        return self.__third_party_packages

    def set_third_party_packages(self, third_party_packages: dict) -> Self:
        self.__third_party_packages = third_party_packages

        return self

    def add_third_party_package(self, third_party_package_name: str, third_party_package_version: str) -> Self:
        self.__third_party_packages[third_party_package_name] = third_party_package_version

        return self

    def get_third_party_package_version(self, third_party_package_name: str) -> str:
        return self.__third_party_packages[third_party_package_name]
