from django.urls import path
from . import views as accounts_views


urlpatterns = [
  path('', accounts_views.home),
  path('contact/', accounts_views.contact),
  path('about/', accounts_views.about),
]