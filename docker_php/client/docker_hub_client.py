import itertools
import math
import multiprocessing
from multiprocessing.pool import ThreadPool
import requests
import requests_cache

from packaging.version import parse
from docker_php.client.exception.docker_hub_client_exception import DockerHubClientException


class DockerHubClient:
    DOCKER_HUB_ENDPOINT = 'https://hub.docker.com/v2/repositories'
    DOCKER_HUB_PAGES_QUERY_TEMPLATE = '/?page={}&page_size={}'
    DOCKER_HUB_TAGS_URI_TEMPLATE = '/{}/{}/tags'

    DOCKER_HUB_MAX_ITEM_PER_PAGE = 100

    def __init__(self):
        requests_cache.install_cache('docker_hub_cache', backend='filesystem', expire_after=360)

    def get_image_tag_list(self, organisation_name: str, project_name: str):
        docker_hub_url = self.__build_url(organisation_name, project_name)
        docker_hub_project_tag_page_url_list = self.__generate_project_tag_page_link_list(docker_hub_url)

        pool = self.__get_thread_pool()
        pool_result = pool.map(self.__get_tag_list, docker_hub_project_tag_page_url_list)

        unique_tag_list = list(set(itertools.chain.from_iterable(pool_result)))
        unique_tag_list.sort(key=parse)

        return unique_tag_list

    def __generate_project_tag_page_link_list(self, docker_hub_url: str) -> list:
        response = self.__get_request(docker_hub_url)

        if 'count' not in response:
            raise DockerHubClientException(response)

        item_count = response['count']

        pages_count = math.ceil(item_count / self.DOCKER_HUB_MAX_ITEM_PER_PAGE)
        urls = []

        for page in range(1, pages_count + 1):
            url_with_page = docker_hub_url + self.DOCKER_HUB_PAGES_QUERY_TEMPLATE.format(page, self.DOCKER_HUB_MAX_ITEM_PER_PAGE)
            urls.append(url_with_page)

        return urls

    def __build_url(self, organisation_name: str, project_name: str) -> str:
        if organisation_name == '' or project_name == '':
            raise ValueError('`organisation_name` and `project_name` shoudn\'t be empty.')

        return self.DOCKER_HUB_ENDPOINT + self.DOCKER_HUB_TAGS_URI_TEMPLATE.format(organisation_name, project_name)

    def __get_tag_list(self, url: str) -> list:
        names = []

        response = self.__get_request(url)

        if 'results' not in response:
            raise DockerHubClientException(response)

        images = response['results']

        for image in images:
            names.append(image['name'])

        return names

    def __get_request(self, url: str) -> dict:
        return requests.get(url).json()

    def __get_thread_pool(self) -> ThreadPool:
        return ThreadPool(multiprocessing.cpu_count())
