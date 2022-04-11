from django.urls import path
from .views import RouteItem, ModifyRouteItem,DeleteRouteItem, CreateRouteItem, CompleteRouteItem


urlpatterns = [
  path('route-item/<str:id>', RouteItem.as_view()),
  path('route-slip/<int:route_slip_id>/modify-route-item/<str:route_item_id>', ModifyRouteItem.as_view()),
  path('route-slip/<int:route_slip_id>/delete-route-item/<str:route_item_id>', DeleteRouteItem.as_view()),
  path('route-item/<str:id>/complete', CompleteRouteItem.as_view()),
  path('route-slip/<int:id>/create-route-item', CreateRouteItem.as_view()),
]