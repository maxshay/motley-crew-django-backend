from rest_framework import serializers
from .models import RouteItem


# from users.models import User
from users.serializers import AssigneeSerializer
from files.serializers import FileSerializer


class SortedRouteItemSerializer(serializers.ListSerializer):
  def to_representation(self, data):
    # data = data.filter(is_archived=False)
    return super(SortedRouteItemSerializer, self).to_representation(data)


# get One
class RouteItemSerializer(serializers.ModelSerializer):
  actionType = serializers.CharField(source='action_type')
  orderNum = serializers.IntegerField(source='order_num')
  completedAt = serializers.DateTimeField(source='completed_at')
  assignee = AssigneeSerializer()
  file = FileSerializer()
  # form field(s)

  class Meta:
    model = RouteItem
    fields = ('id', 'assignee', 'actionType', 'orderNum', 'complete', 'comments', 'completedAt', 'file',)

class CreateRouteItemSerializer(serializers.ModelSerializer):
  actionType = serializers.CharField(source='action_type')
  orderNum = serializers.IntegerField(source='order_num')

  class Meta:
    model = RouteItem
    fields = ('id', 'assignee', 'actionType', 'orderNum', 'complete', 'comments')