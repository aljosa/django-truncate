#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'django-truncate',
    version = '0.1.5',
    description = "django-truncate - truncate template filter",
    long_description = open('README.rst').read(),
    author = 'Aljosa Mohorovic',
    author_email = 'aljosa.mohorovic@gmail.com',
    url='http://github.com/aljosa/django-truncate/',
    packages = find_packages(),
    include_package_data = True,
    license = "MIT License",
    keywords = "django truncate filter",
    platforms = ['any'],
)
