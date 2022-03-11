from django.urls import path
from .views import RouteSlips


urlpatterns = [
  path('route-slips', RouteSlips.as_view()),
]