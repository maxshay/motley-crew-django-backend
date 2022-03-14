from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from motleycrew_backend.permissions import IsOwner

# models
from .models import RouteSlip as RouteSlipModel
# from .models import File as FileModel
# from users.models import User
# from folders.models import Folder as FolderModel

# serializers
from .serializers import RouteSlipSerializer
# from .serializers import FileSerializer, CreateFileSerializer, FilesSerializer
# from folders.serializers import FolderSerializer


# TODO: update the update method to allow reordering of receipients (RouteSlipItems)
# TODO: add no-longer-able-to-modify field, check if route slip already started
# TODO: ensure update rest of fields work
class RouteSlip(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwner,)
  queryset = RouteSlipModel.objects.all()
  serializer_class = RouteSlipSerializer
  lookup_field = 'id'


# TODO: add permission classes
class RouteSlips(generics.ListAPIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = RouteSlipSerializer
  queryset = RouteSlipModel.objects.all()

  # def get_queryset(self):
  #   user = self.request.user
  #   return FolderModel.objects.filter(owner=user)