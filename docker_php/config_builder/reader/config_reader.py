import yaml

from os.path import exists
from yaml import SafeLoader
from docker_php import contants
from packaging.version import parse


class ConfigReader:
    COMMON_CONFIG_NAME = 'common'
    THIRD_PARTY_PACKAGES_FILE_NAME = 'third-party-packages'
    THIRD_PARTY_PACKAGES_KEY = 'third-party-packages'

    def get_config_data_by_distro(self, distro: str):
        distro_config_path = self.__get_config_path(distro)
        common_config_path = self.__get_config_path(self.COMMON_CONFIG_NAME)
        third_party_config_path = self.__get_config_path(self.THIRD_PARTY_PACKAGES_FILE_NAME)

        distro_data = self.__get_data_from_yml_file(distro_config_path)
        common_data = self.__get_data_from_yml_file(common_config_path)
        third_party_data = self.__get_data_from_yml_file(third_party_config_path)

        result = common_data

        for key, params in distro_data.items():
            if key not in result:
                result[key] = params
                continue

            merged_value = result[key] + params
            result[key] = list(set(merged_value))

        for key, params in result.items():
            if type(params) != 'list':
                continue

            params.sort(key=parse)
            result[key] = params

        result[self.THIRD_PARTY_PACKAGES_KEY] = third_party_data

        return result

    def __get_config_path(self, config_name: str) -> str:
        config_file_path = contants.CONFIG_PATH + config_name + '.yml'
        file_exists = exists(config_file_path)

        if file_exists is False:
            raise Exception(f'Config file is not exist: {config_file_path}')

        return config_file_path

    def __get_data_from_yml_file(self, path: str) -> dict:
        with open(path) as f:
            return yaml.load(f, Loader=SafeLoader)
