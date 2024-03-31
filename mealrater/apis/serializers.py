from rest_framework import serializers
from .models import Meal,Rate


class MealSerializer (serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title' ,'description')



class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'stars', 'user', 'meal')