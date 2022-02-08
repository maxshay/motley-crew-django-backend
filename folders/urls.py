from django.urls import path
from .views import GetAllFolders, CreateFolder


urlpatterns = [
  path('folders', GetAllFolders.as_view()),
  path('folder/create', CreateFolder.as_view()),
  # path('folder/:id', GetFolder.as_view()),
  # path('folder/:id', DeleteFolder.as_view()),
]