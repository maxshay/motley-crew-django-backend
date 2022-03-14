from django.urls import path
from .views import RouteSlips, RouteSlip


urlpatterns = [
  path('route-slips', RouteSlips.as_view()),
  path('route-slip/<int:id>', RouteSlip.as_view()),
]