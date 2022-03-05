from django.urls import path
from .views import Files, File, CreateFile


urlpatterns = [
  path('files', Files.as_view()),
  path('file/<int:id>', File.as_view()), # GET, PUT, DELETE
  path('folder/<int:id>/create-file', CreateFile.as_view()),
]