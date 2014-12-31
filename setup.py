# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Sat Oct  4 18:44:56 2014 (+0200)
# Version: 0.1
# Last-Updated: Wed Dec 31 18:24:24 2014 (+0200)
#           By: Ioannis Pinakoulakis
#     Update #: 4
# Description:
# *******************************************************************
# Keywords: setuptools
# *******************************************************************
#
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
    platforms='any',
    install_requires=['Flask', 'requests'],
    zip_safe=False,
    package_dir = {'':'.'},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: Mail :: Mailgun',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
