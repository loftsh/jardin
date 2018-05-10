#!/usr/bin/python3

import sys
import pigpio

import logging
from logging.config import dictConfig

from requests import get
import django

django.setup()
dictConfig(django.conf.settings.LOGGING)
logger = logging.getLogger('jardin')


ip = get('https://api.ipify.org').text

logger.debug('My public IP address is: {}'.format(ip))
