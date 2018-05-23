import django_filters
from django.db import models
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

import aquaponie.views as views


router = routers.DefaultRouter()
router.register(r'pump_state', views.PumpStateView)
router.register(r'temperature', views.TemperatureView)
router.register(r'water_level', views.WaterLevelView)

urlpatterns = [
    path('', views.allTemperature),
    path('api/', include(router.urls)),
]
