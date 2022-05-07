import uuid
from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import RouteItem as RouteItemModel
from files.models import File as FileModel
from form_fields.serializers import FormFieldSerializer
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
  
  def post(self, request, id, format=None):
    body = request.data

    # GETTING THE ROUTE SLIP AND THE FILE REFERENCE FROM THE REQUEST
    try:
      route_slip = RouteSlipModel.objects.get(id=id) # try to get the Route Slip reference
      print(f'[DEBUG] > queue: {route_slip.route_items_queue}')
    except RouteSlipModel.DoesNotExist:
      msg = f'Route slip {id} Not found'
      return Response({'detail': msg}, status=status.HTTP_404_NOT_FOUND)

    file_id = body.get('fileId', None)
    if file_id is None: return Response({'fileId': ['fileId is required']}, status=400)
    
    try:
      file_instance = FileModel.objects.get(id=file_id) # try to get the File reference
    except FileModel.DoesNotExist:
      msg = f'File {file_id} Not found'
      return Response({'detail': msg}, status=status.HTTP_404_NOT_FOUND)


    form_fields = body.pop('formFields', None) # the form_fields before we send to the route item serializer
    print(f'[DEBUG] > {form_fields=}')

    # CREATING THE ROUTE ITEM HERE
    body['orderNum'] = 234
    body['route_slip_id'] = route_slip.id
    body['file'] = file_instance.id
    route_item_temp = CreateRouteItemSerializer(data=body)
    print(f'[DEBUG] > valid={route_item_temp.is_valid(raise_exception=True)}')
    print(f'[DEBUG] > {route_item_temp.validated_data=}')
    route_item_created = route_item_temp.save() # save the route item

    # return Response({'message': 'remove me'})
    # HERE WE'RE CREATING THE FORM FIELDS FOR THE FILE AND THE ROUTE ITEM
    if not form_fields or len(form_fields) < 1:
      return Response({'formFields': ['Must be atleast one form field attached to a route item']})

    # for each form field,
    form_fields_serialized = []
    for form_field in form_fields:
      form_field['file'] = file_instance.id # attaching file
      form_field['route_item'] = route_item_created.id # attaching route item
      f = FormFieldSerializer(data=form_field) # creating
      form_fields_serialized.append(FormFieldSerializer(data=form_field)) # adding to temp list


    for f in form_fields_serialized:
      f.is_valid(raise_exception=True)
      f.save() # save it

    # HERE WE APPEND THE ROUTE ITEM TO THE ROUTE SLIP QUEUE
    route_slip.route_items_queue.append(route_item_created.id)
    route_slip.save()
    return Response({'ok': 'hello'})


