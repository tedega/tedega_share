#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "tedega_view",
    "tedega_storage",
    "passlib",
    "pyjwt"
    # TODO: put package requirements here
]

test_requirements = [
    "pytest-sqlalchemy"
    # TODO: put package test requirements here
]

setup(
    name='tedega_share',
    version='0.1.0',
    description="Core libraries of the Tedega framework",
    long_description=readme + '\n\n' + history,
    author="Torsten Irländer",
    author_email='torsten.irlaender@googlemail.com',
    url='https://github.com/toirl/tedega_share',
    packages=[
        'tedega_share',
    ],
    package_dir={'tedega_share':
                 'tedega_share'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tedega_share',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
