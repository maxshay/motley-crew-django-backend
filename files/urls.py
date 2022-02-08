from django.urls import path
from .views import File


urlpatterns = [
  path('files', File.as_view()),
  path('file', File.as_view()),
]