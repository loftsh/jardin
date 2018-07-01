#!/usr/bin/python3

import sys, os
import re
import time
import logging
from statistics import mean, median

import RPi.GPIO as rpi

sys.path.append('/srv/jardin')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jardin.settings")
import django
django.setup()

from django.utils import timezone

from aquaponie.models import WaterLevel


origin = 20.7
repet = 10
time_sleep = 0.12

trig = 20
echo = 21


def measure_level():
    rpi.output(trig, 0)
    time.sleep(5/1000000.0)
    rpi.output(trig, 1)
    time.sleep(10/1000000.0)
    rpi.output(trig, 0)

    beginLoop = time.perf_counter()
    while rpi.input(echo) == 0:  ## Emission de l'ultrason
        debutImpulsion = time.perf_counter()
        if debutImpulsion - beginLoop > 0.01:
            raise ValueError("Timeout")

    beginLoop = time.perf_counter()
    while rpi.input(echo) == 1:   ## Retour de l'Echo
        finImpulsion = time.perf_counter()
        if finImpulsion - beginLoop > 0.01:
            raise ValueError("Timeout")

    distance = round((finImpulsion - debutImpulsion) * 340.0 * 100.0 / 2.0, 2)
    return distance


def take_measures(repet, verbose=False):

    val = []
    for x in range(repet):
        time.sleep(time_sleep) # sleep must be > 60 ms

        try:
            distance = measure_level()
        except ValueError:
            pass
        else:
            val.append(distance)

        if verbose:
            print(distance)
    return val

rpi.setmode(rpi.BCM)
rpi.setup(trig, rpi.OUT)
rpi.setup(echo, rpi.IN)
val = take_measures(repet, verbose=False)
rpi.cleanup()

level2 = WaterLevel()
level2.date = timezone.now()
level2.level = origin - median(val)
level2.bac = "culture_med"
level2.save()
print("Niveau d'eau median {}".format(origin - median(val)))
