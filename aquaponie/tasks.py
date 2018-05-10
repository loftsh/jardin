import os
import logging
from datetime import datetime

import django
from pigpio import pi
from django_rq import job
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

logger = logging.getLogger(__name__)

@job
def ebb_rise():
    p = pi()
    print("Je monte !")
    logger.info("Marrée montante !")
    p.write(6,1)
    return

@job
def ebb_lower():
    p = pi()
    print("Je descends !")
    logger.info("Marrée descendante !")
    p.write(6,0)
    return

