from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import RouteItem as RouteItemModel
from route_slips.models import RouteSlip as RouteSlipModel
from .serializers import RouteItemSerializer, CreateRouteItemSerializer

from motleycrew_backend.permissions import IsAssignee, IsOwner

# for getting, can be route slip owner or route item assignee
class RouteItem(generics.RetrieveAPIView):
  # permission_classes = (IsAssignee, IsOwner)
  permission_classes = (permissions.AllowAny,)
  queryset = RouteItemModel.objects.all()
  serializer_class = RouteItemSerializer
  lookup_field = 'id'


# for updating or deleting, only for route slip owner
class ModifyRouteItem(generics.UpdateAPIView):
  serializer_class = RouteItemSerializer

  def get_object(self):
    try:
      route_slip = RouteSlipModel.objects.get(pk=self.kwargs.get('route_slip_id'))
    except RouteSlipModel.DoesNotExist as e:
      raise Http404
    self.check_object_permissions(self.request, route_slip)
    # get route item and return it
    route_item = get_object_or_404(RouteItemModel, id=self.kwargs.get('route_item_id'))
    return route_slip

  # check if route slip is started before making changes
  
  # def perform_update(self, serializer):
  #   serializer.save()
  #   pass


# for updating or deleting, only for route slip owner
class DeleteRouteItem(generics.DestroyAPIView):
  serializer_class = RouteItemSerializer

  def get_object(self):
    # get and check folder existance and permissions
    try:
      route_slip = RouteSlipModel.objects.get(pk=self.kwargs.get('route_slip_id'))
    except RouteSlipModel.DoesNotExist as e:
      raise Http404
    self.check_object_permissions(self.request, route_slip)


    # check if route slip is started before making changes

    # get route item and return it
    route_item = get_object_or_404(RouteItemModel, id=self.kwargs.get('route_item_id'))
    return route_item


# mark as complete, only for assginee
class CompleteRouteItem(APIView):
  permission_classes = (IsAssignee,)
  serializer_class = RouteItemSerializer
  def put(self, request, id):

    route_item = get_object_or_404(RouteItemModel, id=id)

    # make sure request user is assignee
    self.check_object_permissions(self.request, route_item)

    # get new 'singed' image from put request
    # (if the action is sign it should store a new image, else the same image should remain)

    # check if complete
    if route_item.complete:
      return Response({'message': f'Route item {id} is already complete'}, status=400)

    # mark complete and save
    route_item.complete = True
    route_item.completed_at = datetime.now()
    route_item.save()

    # get route slip and assign next route time
    # notify all necessary recipients


    route_item_serialized = RouteItemSerializer(route_item)
    return Response(route_item_serialized.data)




class CreateRouteItem(APIView):
  # serializer_class = CreateRouteItemSerializer
  
  def post(self, request, format=None):
    body = request.data




    return Response({'ok': 'hello'})


  '''
  def get_object(self):
    try:
      slip = RouteSlipModel.objects.get(pk=self.kwargs.get('id'))
    except RouteSlipModel.DoesNotExist as e:
      raise Http404
    self.check_object_permissions(self.request, slip)
    return slip
  

  # when adding new route item
  # check priority or step
  # add file/folder permissions to file
  # add to list of shared
  # else?

  def perform_create(self, serializer):
    route_slip = self.get_object()
    serializer.save(route_slip_id=route_slip)

  '''

