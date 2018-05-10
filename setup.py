#!/usr/bin/env python

from distutils.core import setup

PACKAGES = ['django']

setup(
    name='Jardin',
    version='10.0',
    description='Jardin project',
    author='Loft jardin',
    author_email='jardin@sh',
    url='loft.sh',
    install_requires=PACKAGES,
)
