import datetime
import logging
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from aquaponie.models import Temperature, WaterLevel

logger = logging.getLogger(__name__)

def allTemperature(request):
    data = list(Temperature.objects.all())
    temperatures = [(str(d.date), d.temperature) for d in data]
    temperatures = list(zip(*temperatures))

    data = list(WaterLevel.objects.filter(bac='culture_med'))
    levels = [(str(d.date), d.level) for d in data]
    levels = list(zip(*levels))

    data = list(WaterLevel.objects.filter(bac='culture_reg'))
    levels2 = [(str(d.date), d.level) for d in data]
    levels2 = list(zip(*levels2))

    return render(
        request, "aquaponie/dashboard.html",
        context={
            'temperatures': json.dumps(temperatures),
            'waterLevels': json.dumps(levels),
            'waterLevels2': json.dumps(levels2),
        }
    )

