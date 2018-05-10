import datetime
import logging
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from aquaponie.models import Temperature, WaterLevel

logger = logging.getLogger(__name__)

def allTemperature(request):
    data = list(WaterLevel.objects.filter(bac='culture'))
    levels = [(str(d.date), d.level) for d in data]
    levels = list(zip(*levels))

    data = list(WaterLevel.objects.filter(bac='culture_mode'))
    levels1 = [(str(d.date), d.level) for d in data]
    levels1 = list(zip(*levels1))

    data = list(WaterLevel.objects.filter(bac='culture_med'))
    levels2 = [(str(d.date), d.level) for d in data]
    levels2 = list(zip(*levels2))

    data = list(WaterLevel.objects.filter(bac='culture_reg'))
    levels3 = [(str(d.date), d.level) for d in data]
    levels3 = list(zip(*levels3))

    return render(
        request, "aquaponie/temperature.html",
        context={
            'waterLevels': json.dumps(levels),
            'waterLevels1': json.dumps(levels1),
            'waterLevels2': json.dumps(levels2),
            'waterLevels3': json.dumps(levels3),
        }
    )

