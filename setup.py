from setuptools import setup, find_packages

setup(
    name='docker_php',
    version='0.1.0',
    packages=find_packages(
        where='.',
    ),
    install_requires=[
        'PyYAML',
        'pylint',
        'typing_extensions',
        'requests',
        'packaging',
        'requests-cache',
        'jinja2',
        'pylint',
    ],
)
