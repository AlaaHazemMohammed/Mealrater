from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RateViewSet

router = routers.DefaultRouter()
# router.register('users', UserViewSet)
router.register('meals', MealViewSet)
router.register('rates', RateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]