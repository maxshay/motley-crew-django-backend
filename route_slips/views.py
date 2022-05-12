from datetime import datetime
from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from motleycrew_backend.permissions import IsOwner
from django.shortcuts import get_object_or_404

from messages.serializers import CreateMessageSerializer

# models
from .models import RouteSlip as RouteSlipModel
# from .models import File as FileModel
# from users.models import User
from folders.models import Folder as FolderModel
from route_items.models import RouteItem as RouteItemModel
from messages.models import Message as MessageModel


# serializers
from .serializers import RouteSlipSerializer, CreateRouteSlipSerializer
# from .serializers import FileSerializer, CreateFileSerializer, FilesSerializer
# from folders.serializers import FolderSerializer


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

  # TODO add name validation for file accessing
  # TODO add routeslip verification

class FinalizeRouteSlip(APIView):
  permission_classes = (permissions.AllowAny,)
  # serializer_class = RouteSlipSerializer

  def post(self, request, id):
    print(self.request.user)
    route_slip = get_object_or_404(RouteSlipModel, id=id)

    if len(route_slip.route_items_queue) < 1:
      return Response({'message': 'route slip must have atleast one route item'}, status=400)
    if route_slip.route_start_time is not None:
      return Response({'message': f'Route Slip {id} is already finalized and started'}, status=400)

    # get first route item from route slip
    # create pop from the queue
    # assign route item to current route item
    # get assignee and create a message

    # TODO: notify first assignees

    next_route_item_id = route_slip.route_items_queue[0]
    next_route_item = RouteItemModel.objects.get(id=next_route_item_id)
    # print(f'{next_route_item=}')
    # print(f'{next_route_item.assignee=}')

    message_body = {
      'message_type': 'notification',
      'contents': 'Blah would like you to sign this',
      'owner': next_route_item.assignee.id,
      # 'file': next_route_item.file.id
      'route_item': next_route_item.id
    }
    message = CreateMessageSerializer(data=message_body)
    message.is_valid(raise_exception=True)
    # print(f'{message.validated_data}')

    message.save()

    route_slip.current_route_item = next_route_item_id
    route_slip.route_start_time = datetime.now()
    route_slip.save()

    return Response({'message': 'started'})


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


class NextRouteSlip(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny,)


  def post(self, request, slip_id, item_id, format=None):

    # get new file
    # upload new file and attach to next route item
    # remove the first route item in queue
    # get next route item in queue
    # notify next route person
    # maybe: update route slip, and formfields

    return Response({'message': 'ok'})