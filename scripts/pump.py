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

from django.utils import timezone

from aquaponie.models import PumpState


logger = logging.getLogger('loft')

PUMP_PIN = 6


def set_pump_state(state):
    p = pigpio.pi()
    p.write(PUMP_PIN, state)
    p.stop()

    logger.info("J'{} la pompe !".format("allume" if state else "éteins"))


def get_pump_state():
    p = pigpio.pi()
    state = p.read(PUMP_PIN)
    p.stop()
    return state


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == "on":
        set_pump_state(1)

    elif len(sys.argv) == 2 and sys.argv[1] == "off":
        set_pump_state(0)

    elif len(sys.argv) == 2 and sys.argv[1] == "save":
        state = get_pump_state()

        pumpStateLog = PumpState()
        pumpStateLog.date = timezone.now()
        pumpStateLog.state = state
        pumpStateLog.save()
        
        logger.debug("La pompe est {}.".format("allumée" if state else "éteinte"))

    else:
        logger.error("Usage {} on | off | save".format(sys.argv[0]))
        sys.exit(1)
