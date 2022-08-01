from docker_php import contants
from docker_php.config_builder.php_tag_builder.php_tag_builder import PhpTagBuilder
from docker_php.config_builder.reader.config_reader import ConfigReader
from docker_php.dto.distro.distro_packages_transfer import DistroPackagesTransfer
from docker_php.dto.distro.distro_transfer import DistroTransfer
from docker_php.dto.dockerfile_transfer import DockerfileTransfer
from docker_php.dto.php.php_transfer import PhpTransfer
from docker_php.dto.php.php_version_transfer import PhpVersionTransfer
from docker_php.dto.third_party_package_transfer import ThirdPartyPackageTransfer


class ConfigBuilder:
    php_tag_builder: PhpTagBuilder
    config_reader: ConfigReader

    def __init__(self, config_reader: ConfigReader, php_tag_builder: PhpTagBuilder):
        self.php_tag_builder = php_tag_builder
        self.config_reader = config_reader

    def build_dockerfile_transfer_by_distro_name_list(self, distro_name: str) -> list[DockerfileTransfer]:
        config_data = self.config_reader.get_config_data_by_distro(distro_name)

        php_version_by_distro_version_list = config_data[contants.CONFIG_PHP_KEY_NAME]
        php_tag_format = config_data[contants.CONFIG_PHP_TAG_FORMAT_KEY_NAME]
        php_extensions = config_data['php-extensions']
        php_pecl_extensions = config_data['php-pecl-extensions']

        distro_packages_transfer = self.__build_distro_packages_transfer(config_data)
        third_party_package_transfer = self.__build_third_party_package_transfer(config_data)

        dockerfile_transfer_list = []

        for distro_version, php_versions in php_version_by_distro_version_list.items():
            distro_transfer = self.__build_distro_transfer(distro_name, distro_version, distro_packages_transfer)

            for php_version in php_versions:
                image_tag = self.php_tag_builder.get_php_tag(php_version, distro_version, php_tag_format)
                php_version_transfer = self.__build_php_version_transfer(image_tag)
                php_transfer = self.__build_php_transfer(php_version_transfer, image_tag, php_extensions, php_pecl_extensions)
                dockerfile_transfer = self.__build_dockefile_transfer(distro_transfer, php_transfer, third_party_package_transfer)

                dockerfile_transfer_list.append(dockerfile_transfer)

        return dockerfile_transfer_list

    def __build_distro_packages_transfer(self, config_data: dict) -> DistroPackagesTransfer:
        return DistroPackagesTransfer(
            config_data['deps-packages'],
            config_data['php-build-deps-packages'],
            config_data['php-run-deps-packages'],
        )

    def __build_distro_transfer(self, distro_name: str, distro_version: str, distro_packages_transfer: DistroPackagesTransfer) -> DistroTransfer:
        return DistroTransfer(
            distro_name,
            distro_version,
            distro_packages_transfer
        )

    def __build_php_transfer(self, php_version_transfer: PhpVersionTransfer, php_image_tag: str, php_extensions: list, php_pecl_extensions: list) -> PhpTransfer:
        return PhpTransfer(
            php_version_transfer,
            php_image_tag,
            php_extensions,
            php_pecl_extensions,
        )

    def __build_dockefile_transfer(self, distro_transfer: DistroTransfer, php_transfer: PhpTransfer, third_party_package_transfer: ThirdPartyPackageTransfer) -> DockerfileTransfer:
        return DockerfileTransfer(distro_transfer, php_transfer, third_party_package_transfer)

    def __build_third_party_package_transfer(self, config_data) -> ThirdPartyPackageTransfer:
        return ThirdPartyPackageTransfer(config_data['third-party-packages'])

    def __build_php_version_transfer(self, image_tag: str) -> PhpVersionTransfer:
        php_version = image_tag.split('-fpm')[0]

        return PhpVersionTransfer(php_version)


