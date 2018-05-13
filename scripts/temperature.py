#!/usr/bin/python3

import sys, os
import re

import pigpio

import logging
from logging.config import dictConfig

sys.path.append('/srv/jardin')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jardin.settings")
import django
django.setup()

from django.utils import timezone

from aquaponie.models import Temperature


# Config logging
logger = logging.getLogger('loft')

w1_path = "/sys/bus/w1/devices/28-051790466dff/w1_slave"

verbose = False
if len(sys.argv) == 2 and sys.argv[1] == "-v":
    verbose = True

try:
    with open(w1_path, 'r') as w1_f:
        data = w1_f.read()

        if not 'YES' in data:
            raise AttributeError("Sensor not initialized.")

        temp = float(re.search('t=(\d+)', data).group(1))/1000
        if verbose:
            logger.info("La température du bac à poissons est de : {}.".format(temp))

        tempLog = Temperature()
        tempLog.date = timezone.now()
        tempLog.temperature = temp
        tempLog.save()

except IOError as error:
    logger.warning("Can not read temperature sensor datas.\n{}".format(error))
except AttributeError as error:
    logger.warning("Can not parse temperature sensor datas.\n{}".format(error))
except Exception as error:
    logger.warning("Error.\n{}".format(error))
