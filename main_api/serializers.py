
from rest_framework import serializers
from .models import cars, rate


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = ["make", "model"]


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = rate
        fields = ["car_id", "rating"]

