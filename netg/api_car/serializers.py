from rest_framework import serializers
from .models import Car, Rate
from django.db.models import Avg
from pprint import pprint


class CarSerializer(serializers.ModelSerializer):

    avg_rating = serializers.SerializerMethodField('calculate_avg_rating')

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def calculate_avg_rating(self, obj):
        if hasattr(obj, 'avg_rating'):
            return obj.avg_rating


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['car_id','rating']


class PopularSerializer(serializers.ModelSerializer):

    rates_number = serializers.SerializerMethodField('calculate_avg_rating')

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']

    def calculate_avg_rating(self, obj):
        if hasattr(obj, 'rates_number'):
            return obj.rates_number
