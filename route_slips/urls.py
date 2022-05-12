from django.urls import path
from .views import RouteSlips, RouteSlip, FinalizeRouteSlip, NextRouteSlip


urlpatterns = [
  path('route-slips', RouteSlips.as_view()),
  path('route-slip/<int:id>', RouteSlip.as_view()),
  path('route-slip/<int:id>/start', FinalizeRouteSlip.as_view()),
  path('route-slip-step/<int:slip_id>/<str:item_id>', NextRouteSlip.as_view()),
]