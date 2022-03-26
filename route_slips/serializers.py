from rest_framework import serializers
from .models import RouteSlip


class ActiveFilteredRouteSlipSerializer(serializers.ListSerializer):
  def to_representation(self, data):
    data = data.filter(is_archived=False)
    return super(ActiveFilteredRouteSlipSerializer, self).to_representation(data)


class ActiveRouteSlipSerializer(serializers.ModelSerializer):
  orderType = serializers.CharField(source='order_type')
  currentId = serializers.IntegerField(source='current_id')
  folderId = serializers.PrimaryKeyRelatedField(source='folder_id', read_only=True)
  isArchived = serializers.BooleanField(source='is_archived')

  class Meta:
    model = RouteSlip
    list_serializer_class = ActiveFilteredRouteSlipSerializer
    fields = ('id', 'orderType', 'currentId', 'folderId', 'isArchived', 'owner')
    read_only_fields = ('id', 'orderType', 'currentId', 'folderId', 'owner')
    # exclude = ['model_a_field', ']


class RouteSlipSerializer(serializers.ModelSerializer):
  orderType = serializers.CharField(source='order_type')
  currentId = serializers.IntegerField(source='current_id')
  folderId = serializers.PrimaryKeyRelatedField(source='folder_id', read_only=True)
  isArchived = serializers.BooleanField(source='is_archived')

  class Meta:
    model = RouteSlip
    fields = ('id', 'orderType', 'currentId', 'folderId', 'isArchived', 'owner')
    read_only_fields = ('id', 'orderType', 'currentId', 'folderId', 'owner')
    # exclude = ['model_a_field', ']


class CreateRouteSlipSerializer(serializers.ModelSerializer):

  class Meta:
    model = RouteSlip
    fields = ('id', 'orderType', 'currentId', 'folderId', 'isArchived', 'owner')
    read_only_fields = ('id', 'orderType', 'currentId', 'folderId', 'owner')