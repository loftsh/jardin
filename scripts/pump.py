#!/usr/bin/python3

import sys
import pigpio
import os

import logging
from logging.config import dictConfig

sys.path.append('/srv/jardin')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jardin.settings")
import django
django.setup()

logger = logging.getLogger('loft')

pump_pin = 6

if len(sys.argv) == 2 and sys.argv[1] == "on":
    state = 1
elif len(sys.argv) == 2 and sys.argv[1] == "off":
    state = 0
else:
    logger.error("Usage {} on | off".format(sys.argv[0]))
    sys.exit(1)

p = pigpio.pi()
p.write(pump_pin, state)
logger.info("J'{} la pompe !".format("allume" if state else "éteins"))
p.stop()
