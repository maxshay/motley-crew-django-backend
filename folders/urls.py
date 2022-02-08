from django.urls import path
from .views import GetAllFolders, CreateFolder, Folder


urlpatterns = [
  path('folders', GetAllFolders.as_view()),
  path('folder/create', CreateFolder.as_view()),
  path('folder/<int:id>', Folder.as_view())
]