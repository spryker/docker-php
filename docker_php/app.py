from docker_php.config_builder.enum.distro import Distro
from docker_php.factory import Factory


class App:
    def __init__(self):
        self.factory = Factory()

    def run(self):
        config_builder = self.factory.get_config_builder()
        dockerfile_render = self.factory.get_dockerfile_render()

        for distro in Distro:
            dockerfile_transfer_list = config_builder.build_dockerfile_transfer_by_distro_name_list(str(distro.value))

            for dockerfile_transfer in dockerfile_transfer_list:
                dockerfile_render.render(dockerfile_transfer)
