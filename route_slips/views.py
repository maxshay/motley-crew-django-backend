from datetime import datetime
from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from motleycrew_backend.permissions import IsOwner
from django.shortcuts import get_object_or_404

# models
from .models import RouteSlip as RouteSlipModel
# from .models import File as FileModel
# from users.models import User
from folders.models import Folder as FolderModel

# serializers
from .serializers import RouteSlipSerializer, CreateRouteSlipSerializer
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

  #TODO add name validation for file accessing
  #TODO add routeslip verification

class FinalizeRouteSlip(APIView):
  permission_classes = (IsOwner,)
  serializer_class = RouteSlipSerializer
  def put(self, request, id):

    route_slip = get_object_or_404(RouteSlipModel, id=id)

    # make sure request user is owner of route slip
    self.check_object_permissions(self.request, route_slip)

    if route_slip.route_start_time is not None:
      return Response({'message': f'Route Slip {id} is already finalized and started'}, status=400)

    route_slip.route_start_time = datetime.now()
    route_slip.save()

    # TODO: notify first assignees

    route_slip_serialized = RouteItemSerializer(route_slip)
    return Response({'ok': 'nice', 'data': route_slip_serialized.data })


class CreateRouteSlip(generics.CreateAPIView):
  permission_classes = (IsOwner,)
  serializer_class = CreateRouteSlipSerializer
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