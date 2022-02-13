from django.urls import path
from .views import Folders, CreateFolder, Folder


urlpatterns = [
  path('folders', Folders.as_view()),
  path('folder/create', CreateFolder.as_view()),
  path('folder/<int:id>', Folder.as_view())
]