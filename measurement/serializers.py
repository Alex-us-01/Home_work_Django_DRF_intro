from rest_framework import serializers

from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    """Информация по измерениям"""
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class MeasurementEntrySerializer(serializers.ModelSerializer):
    """Информация для ввода измерения"""
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']


class SensorSerializer(serializers.ModelSerializer):
    """Информация по датчикам"""
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorEditSerializer(serializers.ModelSerializer):
    """Изменение информации по датчику"""
    class Meta:
        model = Sensor
        fields = ['description']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Информация по датчику"""
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
