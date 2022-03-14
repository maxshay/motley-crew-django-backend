from rest_framework import serializers
from .models import RouteSlip


class RouteSlipSerializer(serializers.ModelSerializer):
  orderType = serializers.CharField(source='order_type')
  currentId = serializers.IntegerField(source='current_id')
  folderId = serializers.PrimaryKeyRelatedField(source='folder_id', read_only=True)
  isArchived = serializers.BooleanField(source='is_archived')


  # owner = serializers.HiddenField(
  #   default=serializers.CurrentUserDefault()
  # )

  class Meta:
    model = RouteSlip
    fields = ('id', 'orderType', 'currentId', 'folderId', 'isArchived', 'owner')
    read_only_fiels = ('id', 'orderType', 'currentId', 'folderId', 'owner')
    # exclude = ['model_a_field', ']