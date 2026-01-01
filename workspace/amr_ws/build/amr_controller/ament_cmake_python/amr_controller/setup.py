from setuptools import find_packages
from setuptools import setup

setup(
    name='amr_controller',
    version='0.0.0',
    packages=find_packages(
        include=('amr_controller', 'amr_controller.*')),
)
