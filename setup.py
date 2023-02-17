#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="micro-logger",
    version="0.1.3",
    package_dir = {'': 'lib'},
    py_modules = [
        'micro_logger',
        'micro_logger_unittest'
    ],
    install_requires=[
        'python-json-logger==2.0.2'
    ],
    url="https://github.com/relations-dil/python-micro-logger",
    author="Gaffer Fitch",
    author_email="micro-logger@gaf3.com",
    description="A JSON logger made for microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license_files=('LICENSE.txt',),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
