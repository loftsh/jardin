import django_filters
from rest_framework import serializers

from aquaponie.models import WaterLevel, PumpState, Temperature


# Filters
class PumpStateFilter(django_filters.FilterSet):
    class Meta:
        model = PumpState
        fields = ['date', 'state']

    date_gt = django_filters.IsoDateTimeFilter(name="date", lookup_expr='gt')
    date_lt = django_filters.IsoDateTimeFilter(name="date", lookup_expr='lt')


class TemperatureFilter(django_filters.FilterSet):
    class Meta:
        model = Temperature
        fields = ['date', 'temperature']

    date_gt = django_filters.IsoDateTimeFilter(name="date", lookup_expr='gt')
    date_lt = django_filters.IsoDateTimeFilter(name="date", lookup_expr='lt')


class WaterLevelFilter(django_filters.FilterSet):
    class Meta:
        model = WaterLevel
        fields = ['date', 'bac', 'level']

    date_gt = django_filters.IsoDateTimeFilter(name="date", lookup_expr='gt')
    date_lt = django_filters.IsoDateTimeFilter(name="date", lookup_expr='lt')


# Serializers
class PumpStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpState
        fields = ('date', 'state')

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
    state = serializers.IntegerField()


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('date', 'temperature')

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")


class WaterLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterLevel
        fields = ('date', 'level', 'bac')

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")
