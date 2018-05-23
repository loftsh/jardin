import datetime
import logging
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from aquaponie.models import Temperature, WaterLevel, PumpState
from aquaponie.helpers import (
    PumpStateSerializer, TemperatureSerializer, WaterLevelSerializer,
    PumpStateFilter, TemperatureFilter, WaterLevelFilter,
)

logger = logging.getLogger(__name__)


class PumpStateView(viewsets.ReadOnlyModelViewSet):
    queryset = PumpState.objects.all()
    serializer_class = PumpStateSerializer
    filter_class = PumpStateFilter


class TemperatureView(viewsets.ReadOnlyModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    filter_class = TemperatureFilter


class WaterLevelView(viewsets.ModelViewSet):
    queryset = WaterLevel.objects.all()
    serializer_class = WaterLevelSerializer
    filter_class = WaterLevelFilter


def allTemperature(request):
    data = list(Temperature.objects.order_by('-date')[:1000])
    temperatures = [(str(d.date), d.temperature) for d in data]
    temperatures = list(zip(*temperatures))

    data = list(PumpState.objects.order_by('-date')[:1000])
    states = [(str(d.date), 1 if d.state else 0) for d in data]
    states = list(zip(*states))

    data = list(WaterLevel.objects.filter(bac='culture_med').order_by('-date')[:1000])
    levels = [(str(d.date), d.level) for d in data]
    levels = list(zip(*levels))

    data = list(WaterLevel.objects.filter(bac='culture_reg').order_by('-date')[:1000])
    levels2 = [(str(d.date), d.level) for d in data]
    levels2 = list(zip(*levels2))

    return render(
        request, "aquaponie/dashboard.html",
        context={
            'temperatures': json.dumps(temperatures),
            'pumpStates': json.dumps(states),
            'waterLevels': json.dumps(levels),
            'waterLevels2': json.dumps(levels2),
        }
    )

