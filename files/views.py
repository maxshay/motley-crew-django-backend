import urllib3
import requests
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from motleycrew_backend.permissions import IsOwner

# models
from .models import File as FileModel
from users.models import User
from folders.models import Folder as FolderModel

# serializers
from .serializers import FileSerializer, CreateFileSerializer, FilesSerializer
from folders.serializers import FolderSerializer

# file scanner script
from scripts.documentformrecognationscript import scan


# think of these as controllers
class File(generics.RetrieveDestroyAPIView):
  permission_classes = (IsOwner,)
  queryset = FileModel.objects.all()
  serializer_class = FileSerializer
  lookup_field = 'id'


class Files(generics.ListAPIView):
  serializer_class = FilesSerializer

  def get_queryset(self):
    user = self.request.user
    return FolderModel.objects.filter(owner=user)



# TODO: get files for single folder
class FolderFiles(generics.RetrieveAPIView):
  permission_classes = (IsOwner,)
  serializer_class = FilesSerializer

  def get_object(self):
    try:
      folder = FolderModel.objects.get(pk=self.kwargs.get('id'))
    except FolderModel.DoesNotExist as e:
      raise Http404
    self.check_object_permissions(self.request, folder)
    return folder

  def get_queryset(self):
    user = self.request.user
    return FolderModel.objects.filter(owner=user)


class CreateFile(generics.CreateAPIView):
  permission_classes = (IsOwner,)
  serializer_class = CreateFileSerializer
  queryset = FolderModel.objects.all()

  def get_object(self):
    try:
      folder = FolderModel.objects.get(pk=self.kwargs.get('id'))
    except FolderModel.DoesNotExist as e:
      raise Http404
    self.check_object_permissions(self.request, folder)
    return folder

  def perform_create(self, serializer):
    parent_folder = self.get_object()
    serializer.save(parent_folder=parent_folder)


#TODO need to add some name validation
#TODO start adding more comments to help with future readability.
class ScanFileTest(APIView):
  def get(self, request, id, format=None):

    f = get_object_or_404(FileModel, id=id)
    contents = requests.get(f.file.url).content
    arr = scan(contents)
    print(arr)
    return Response({'points': arr})
