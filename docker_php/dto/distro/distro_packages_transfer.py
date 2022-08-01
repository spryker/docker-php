from typing_extensions import Self


class DistroPackagesTransfer:
    __deps_packages: list
    __php_build_deps_packages: list
    __php_run_deps_packages: list

    def __init__(
        self,
        deps_packages: list,
        php_build_deps_packages: list,
        php_run_deps_packages: list
    ):
        self.__deps_packages = deps_packages
        self.__php_build_deps_packages = php_build_deps_packages
        self.__php_run_deps_packages = php_run_deps_packages

    def get_deps_packages(self) -> list:
        return self.__deps_packages

    def get_php_build_deps_packages(self) -> list:
        return self.__php_build_deps_packages

    def get_php_run_deps_packages(self) -> list:
        return self.__php_run_deps_packages

    def set_deps_packages(self, deps_packages: list) -> Self:
        self.__deps_packages = deps_packages

        return self

    def set_php_build_deps_packages(self, php_build_deps_packages: list) -> Self:
        self.__php_build_deps_packages = php_build_deps_packages

        return self

    def set_php_run_deps_packages(self, php_run_deps_packages: list) -> Self:
        self.__php_run_deps_packages = php_run_deps_packages

        return self
