#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='PyDE',
    version='0.0.0',
    description='A Pythonic experiment in Differential Equation solving. Not currently intended as a serious piece of software; mostly a fun little experiment.',
    long_description=readme + '\n\n' + history,
    author='Daniel Williams, Liam Wright',
    author_email='mail@daniel-williams.co.uk',
    url='https://github.com/transientlunatic/PyDE',
    packages=[
        'PyDE',
    ],
    package_dir={'PyDE':
                 'PyDE'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='PyDE',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)