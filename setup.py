# -*- coding: utf-8 -*-

# p8fy / by luisfl.me


from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'p8fy',
    version = '1.0.0',
    description = 'Transform an image to use PICO-8\'s color palette',
    long_description = readme,
    author = 'Luis Fariña',
    author_email = 'luis@luisfl.me',
    url = 'https://github.com/lui5fl/p8fy',
    license = license,
    packages = find_packages(exclude = ('tests', 'docs'))
)