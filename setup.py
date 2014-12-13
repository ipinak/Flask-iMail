# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Filename: setup.py
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Maintainer:
# Created: Sat Oct  4 18:44:56 2014 (+0200)
# Version:
# Last-Updated:
#           By:
#     Update #: 0
# Description:
# *******************************************************************
# Keywords: setuptools
# *******************************************************************
__author__ = 'ipinak'

from setuptools import setup

setup(
    name='flask-iMail',
    version='0.1',
    url='http://github.com/ipinak/Flask-iMail',
    license='BSD',
    author='Ioannis Pinakoulakis',
    maintainer='Ioannis Pinakoulakis',
    description='Mailgun integration for Flask.',
    py_modules=['mailgun_api', 'uri'],
    include_package_data=True,
    platforms='any',
    install_requires=['Flask', 'requests'],
    zip_safe=False,
    package_dir = {'.':'.'},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: Mail :: Mailgun',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)