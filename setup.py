#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Peopl3s
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2021 Peopl3s
"""

version = '0.1.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='JSPTH',
    version=version,

    author='Artur Maievskyi',
    author_email='artr.mayevski@gmail.com',

    description=(
        u'Python module, importing some JS functions and math code '
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Peopl3s/club_house_api',
    download_url='https://github.com/Peopl3s/club-house-api/archive/main.zip'

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['club_house_api'],
    install_requires=['aiohttp', 'aiofiles'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
