import re
from docker_php.client.docker_hub_client import DockerHubClient
from packaging.version import parse


class PhpTagBuilder:
    docker_hub_client: DockerHubClient

    def __init__(self, docker_hub_client: DockerHubClient):
        self.docker_hub_client = docker_hub_client

    def get_php_tag(self, php_version: str, distro_version: str, php_tag_format: str) -> str:
        php_version_regexp = self.__build_php_version_regexp_template(php_version, distro_version, php_tag_format)

        return self.__find_latest_php_version(php_version_regexp)

    def __find_latest_php_version(self, php_version_regexp: str):
        image_list = self.docker_hub_client.get_image_tag_list('library', 'php')
        versions = []

        for image_name in image_list:
            match = re.search(php_version_regexp, image_name)

            if match:
                versions.append(image_name)

        if not versions:
            return ''

        versions.sort(key=parse)

        return versions.pop()

    def __build_php_version_regexp_template(self, php_version: str, distro_version: str, php_tag_format: str):
        php_version = str(php_version)
        tag = php_tag_format.replace('{{distro_version}}', distro_version)
        version_regexp = '^{}[0-9][0-9.]*'
        distro_version = ''

        match len(re.findall('\.', php_version)):
            case 2:
                distro_version = php_version
            case 1 | 0:
                distro_version = version_regexp.format(php_version + '.')

        return tag.replace('{{php_version}}', distro_version)
