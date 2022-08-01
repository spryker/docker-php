from jinja2 import Environment, PackageLoader, select_autoescape

from docker_php.client.docker_hub_client import DockerHubClient
from docker_php.config_builder.config_builder import ConfigBuilder
from docker_php.config_builder.php_tag_builder.php_tag_builder import PhpTagBuilder
from docker_php.config_builder.reader.config_reader import ConfigReader
from docker_php.render.dockerfile_render import DockerfileRender


class Factory:
    def get_config_builder(self):
        return ConfigBuilder(
            self.get_config_reader(),
            self.get_php_tag_builder()
        )

    def get_docker_hub_client(self):
        return DockerHubClient()

    def get_dockerfile_render(self):
        return DockerfileRender(
            self.get_jinja_environment()
        )

    def get_config_reader(self):
        return ConfigReader()

    def get_php_tag_builder(self):
        return PhpTagBuilder(self.get_docker_hub_client())

    def get_jinja_environment(self):
        return Environment(
            loader=PackageLoader("docker_php"),
            autoescape=select_autoescape()
        )
