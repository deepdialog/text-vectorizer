#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""pip setup config."""

#############################################
# File Name: setup.py
# Author: TextVectorizer
# Mail: thebotbot@sina.com
# Created Time: 2019-05-29
#############################################

import os
from setuptools import setup, find_packages

INSTALL_REQUIRES = [x.strip() for x in open(os.path.join(
    os.path.realpath(os.path.dirname(__file__)),
    'requirements.txt'
)).read().split('\n') if len(x.strip())]

VERSION = os.path.join(
    os.path.realpath(os.path.dirname(__file__)),
    'text_vectorizer',
    'version.txt'
)

setup(
    name='text_vectorizer',
    version=open(VERSION, 'r').read().strip(),
    keywords=('bot',),
    description='NLP tool',
    long_description='Dialog System',
    license='Private',
    url='https://github.com/deepdialog/text-vectorizer',
    author='deepdialog',
    author_email='thebotbot@sina.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=INSTALL_REQUIRES
)
