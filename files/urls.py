from django.urls import path
from .views import Files, File, CreateFile


urlpatterns = [
  path('files', Files.as_view()),
  path('file/<int:id>', File.as_view()),
  path('file/create', CreateFile.as_view()),
]