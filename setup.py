#!/usr/bin/env python

from distutils.core import setup

PACKAGES = [
    'Django',
    'django-rq',
    'django-rq-scheduler',
    'djangorestframework',
    'django-filter',
    'redis',
    'rq',
    'rq-scheduler',
    'python-telegram-handler',
    'pigpio',
]

TEST_PACKAGES = PACKAGES + [
    'flake8',
    'flake8-docstrings',
    'flake8-print',
    'flake8-import-order',
    'flake8-strict',
    'flake8-builtins',
]

EXTRAS = {
    'test': TEST_PACKAGES,
}

setup(
    name='Jardin',
    version='10.0',
    description='Jardin project',
    author='Loft jardin',
    author_email='jardin@sh',
    url='loft.sh',
    install_requires=PACKAGES,
    test_requires=TEST_PACKAGES,
    extras_require=EXTRAS,
)
