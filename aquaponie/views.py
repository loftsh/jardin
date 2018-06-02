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
    ordering_fields = ('date',)


class TemperatureView(viewsets.ReadOnlyModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    filter_class = TemperatureFilter
    ordering_fields = ('date',)


class WaterLevelView(viewsets.ModelViewSet):
    queryset = WaterLevel.objects.all()
    serializer_class = WaterLevelSerializer
    filter_class = WaterLevelFilter
    ordering_fields = ('date',)


def allTemperature(request):
    data = reversed(Temperature.objects.order_by('-date')[:1000])
    temperatures = [{'date': str(d.date), 'temperature': d.temperature} for d in data]

    data = reversed(PumpState.objects.order_by('-date')[:1000])
    states = [{'date': str(d.date), 'state': 1 if d.state else 0} for d in data]

    data = reversed(WaterLevel.objects.filter(bac='culture_med').order_by('-date')[:1000])
    levels = [{'date': str(d.date), 'level': d.level} for d in data]

    return render(
        request, "aquaponie/dashboard.html",
        context={
            'temperatures': json.dumps(temperatures),
            'pumpStates': json.dumps(states),
            'waterLevels': json.dumps(levels),
        }
    )

