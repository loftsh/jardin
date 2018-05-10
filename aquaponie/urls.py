from django.contrib import admin
from django.urls import path, re_path, include

from aquaponie.views import allTemperature

urlpatterns = [
    path('', allTemperature)
]
