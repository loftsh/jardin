import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from datetime import datetime
from pigpio import pi

from django_rq import job

import django
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

import logging

logger = logging.getLogger(__name__)


@job
def marree_montante():
    p=pi()
    print("Je monte !")
    logger.info("Marrée montante !")
    p.write(6,1)
    return

@job
def marree_descendante():
    p=pi()
    print("Je descends !")
    logger.info("Marrée descendante !")
    p.write(6,0)
    return

