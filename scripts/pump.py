#!/usr/bin/python3

import sys
import os
import logging

import pigpio

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
    before = p.read(PUMP_PIN)

    p.write(PUMP_PIN, state)
    p.stop()

    pumpBefore = PumpState()
    pumpBefore.date = timezone.now()
    pumpBefore.state = before
    pumpBefore.save()

    pumpNow = PumpState()
    pumpNow.date = timezone.now()
    pumpNow.state = state
    pumpNow.save()

    logger.info("J'{} la pompe !".format("allume" if state else "éteins"))


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == "on":
        set_pump_state(1)

    elif len(sys.argv) == 2 and sys.argv[1] == "off":
        set_pump_state(0)

    else:
        logger.error("Usage {} on | off".format(sys.argv[0]))
        sys.exit(1)
