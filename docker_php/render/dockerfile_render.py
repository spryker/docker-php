import os
from pprint import pprint

from jinja2 import Environment

from docker_php.contants import BUILD_PATH
from docker_php.dto.dockerfile_transfer import DockerfileTransfer


class DockerfileRender:
    def __init__(self, jinja_env: Environment):
        self.jinja_env = jinja_env

    def render(self, dockerfile_transfer: DockerfileTransfer) -> None:
        template = self.jinja_env.get_template('dockerfile/Dockerfile.tmpl')

        dockerfile = template.render({
            'dockerfile_transfer': dockerfile_transfer,
        })
        file_path = self.__build_file_path(dockerfile_transfer)
        open(file_path, "w").write(dockerfile)

    def __build_file_path(self, dockerfile_transfer: DockerfileTransfer) -> str:
        php_version_path_template = '{}.{}'
        dockerfile_path_template = BUILD_PATH + '{}' + os.sep + '{}' + os.sep + '{}' + os.sep

        php_version = php_version_path_template.format(
            dockerfile_transfer.get_php_transfer().get_version_trasfer().get_major_version(),
            dockerfile_transfer.get_php_transfer().get_version_trasfer().get_minor_version(),
        )

        directory_path = dockerfile_path_template.format(
            dockerfile_transfer.get_distro_transfer().get_name(),
            dockerfile_transfer.get_distro_transfer().get_version(),
            php_version
        )

        os.makedirs(os.path.abspath(directory_path), exist_ok=True)

        return directory_path + 'Dockerfile'
