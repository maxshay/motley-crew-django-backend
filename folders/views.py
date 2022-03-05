from rest_framework.response import Response
from rest_framework import generics, permissions

from .permissions import IsOwner
from .serializers import FolderSerializer
from .models import Folder as FolderModel
from users.models import User as UserModel

# dev
# import logging

class Folders(generics.ListAPIView):
  queryset = FolderModel.objects.all()
  serializer_class = FolderSerializer

  def get_queryset(self):
    user = self.request.user
    return FolderModel.objects.filter(owner=user)


class Folder(generics.RetrieveUpdateDestroyAPIView):
  queryset = FolderModel.objects.all()
  serializer_class = FolderSerializer
  permission_classes = (IsOwner,)
  lookup_field = 'id'


class CreateFolder(generics.CreateAPIView):
  permission_classes = (IsOwner,)
  serializer_class = FolderSerializer
