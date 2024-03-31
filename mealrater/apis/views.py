from django.shortcuts import render
from rest_framework import  viewsets
from .models import Meal ,Rate
from .serializers import MealSerializer , RateSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer