#!/usr/bin/python3

import sys, os
import re
import time
import logging 
from statistics import mean, median

# statistics.mode raise error when the mode is not unique
# replace with a gentler mode
from collections import Counter
def mode(values):
    c = Counter(values)
    modes = [x[0] for x in c.most_common() if x[1] == c.most_common()[0][1]]
    return modes[0]

import pigpio

sys.path.append('/srv/jardin')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jardin.settings")
import django
django.setup()

from django.utils import timezone

from aquaponie.models import WaterLevel


origin = 20.7
repet = 50
time_sleep = 0.12

def regress(values):
    measure = mode([round(x, 1) for x in values])
    #reg_coef = [21.82509431, -0.96010228]
    #reg_coef = [21.239, -1.0878]
    reg_coef = [22.52, -1.41, 0.01884]
    return sum([x * measure**i for i, x in enumerate(reg_coef)])


trig = 20
echo = 21


def measure_level():
    p.write(trig, 0)
    time.sleep(5/1000000.0)
    p.write(trig, 1)
    time.sleep(10/1000000.0)
    p.write(trig, 0)

    beginLoop = time.perf_counter()
    while p.read(echo) == 0:  ## Emission de l'ultrason
        debutImpulsion = time.perf_counter()
        if debutImpulsion - beginLoop > 0.01:
            raise ValueError("Timeout")

    beginLoop = time.perf_counter()
    while p.read(echo) == 1:   ## Retour de l'Echo
        finImpulsion = time.perf_counter()
        if finImpulsion - beginLoop > 0.01:
            raise ValueError("Timeout")

    distance = round((finImpulsion - debutImpulsion) * 340.0 * 100.0 / 2.0, 2)
    return distance


def take_measure(repet, verbose=False):

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

p = pigpio.pi()
val = take_measure(repet, verbose=False)
p.stop()


for raw_data in val:
    raw_level = WaterLevel()
    raw_level.date = timezone.now()
    raw_level.level = raw_data
    raw_level.bac = 'culture_raw'
    raw_level.save()

level = WaterLevel()
level.date = timezone.now()
level.level = origin - mode(val)
level.bac = "culture_mode"
level.save()
print("Niveau d'eau mode {}".format(origin - mode(val)))
level2 = WaterLevel()
level2.date = timezone.now()
level2.level = origin - median(val)
level2.bac = "culture_med"
level2.save()
print("Niveau d'eau median {}".format(origin - median(val)))
level3 = WaterLevel()
level3.date = timezone.now()
level3.level = regress(val)
level3.bac = "culture_reg"
level3.save()
print("Niveau d'eau estimé par regression {}".format(regress(val)))
print("mode: {}".format(mode(val)))
