from rest_framework import serializers
from .models import RouteSlip

from route_items.serializers import RouteItemSerializer

class ActiveFilteredRouteSlipSerializer(serializers.ListSerializer):
  def to_representation(self, data):
    data = data.filter(is_archived=False)
    return super(ActiveFilteredRouteSlipSerializer, self).to_representation(data)


class ActiveRouteSlipSerializer(serializers.ModelSerializer):
  orderType = serializers.CharField(source='order_type')
  currentRouteItem = serializers.IntegerField(source='current_route_item')

  folderId = serializers.StringRelatedField(source='folder_id')

  isArchived = serializers.BooleanField(source='is_archived')
  routeItems = RouteItemSerializer(source='routeitem_set', many=True)
  routeItemsQueue = serializers.ListField(child=serializers.UUIDField(), source='route_items_queue')
  owner = serializers.StringRelatedField()

  class Meta:
    model = RouteSlip
    list_serializer_class = ActiveFilteredRouteSlipSerializer
    fields = ('id', 'orderType',  'routeItemsQueue', 'currentRouteItem', 'folderId', 'isArchived', 'owner', 'routeItems')
    read_only_fields = ('id', 'orderType', 'currentRouteItem', 'folderId', 'owner')
    # exclude = ['model_a_field', ']


class RouteSlipSerializer(serializers.ModelSerializer):
  orderType = serializers.CharField(source='order_type')
  currentRouteItem = serializers.IntegerField(source='current_route_item')

  # folderId = serializers.PrimaryKeyRelatedField(source='folder_id', read_only=True)
  folderId = serializers.StringRelatedField(source='folder_id')
  isArchived = serializers.BooleanField(source='is_archived')

  routeItems = RouteItemSerializer(source='routeitem_set', many=True)
  routeItemsQueue = serializers.ListField(child=serializers.UUIDField(), source='route_items_queue')
  owner = serializers.StringRelatedField()
  

  class Meta:
    model = RouteSlip
    fields = ('id', 'orderType',  'routeItemsQueue', 'currentRouteItem', 'folderId', 'isArchived', 'owner', 'routeItems')
    # read_only_fields = ('id', 'orderType', 'currentRouteItemId', 'folderId', 'owner')


class CreateRouteSlipSerializer(serializers.ModelSerializer):

  class Meta:
    model = RouteSlip
    fields = ('id', 'orderType', 'currentId', 'folderId', 'isArchived', 'owner')
    read_only_fields = ('id', 'orderType', 'currentId', 'folderId', 'owner')