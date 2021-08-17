"""
Setup file
Author : Damien Michelle
date : 13/08/2021
"""
from setuptools import setup

setup(
    name='etl_premium_clients',
    author='Damien Michelle',
    author_email='damienmichelle1994@hotmail.com',
    version='1.0',
    packages=['etl_premium_clients'],
    include_package_data=True,
    python_requires='~=3.8',
    description='Transforms and optimize sqlite db',
    license='LICENSE',
    entry_points={
        'console_scripts': ['etl_premium_clients=etl_premium_clients.main:main']
    },
    long_description=open('README.md').read()
)
