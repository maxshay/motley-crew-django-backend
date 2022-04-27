from rest_framework import serializers
from .models import RouteItem

# from users.models import User
from users.serializers import AssigneeSerializer


# get One
class RouteItemSerializer(serializers.ModelSerializer):
  actionType = serializers.CharField(source='action_type')
  orderNum = serializers.IntegerField(source='order_num')
  completedAt = serializers.DateTimeField(source='completed_at')
  assignee = AssigneeSerializer()

  class Meta:
    model = RouteItem
    fields = ('id', 'assignee', 'actionType', 'orderNum', 'complete', 'comments', 'completedAt')

class CreateRouteItemSerializer(serializers.ModelSerializer):
  actionType = serializers.CharField(source='action_type')
  orderNum = serializers.IntegerField(source='order_num')

  class Meta:
    model = RouteItem
    fields = ('id', 'assignee', 'actionType', 'orderNum', 'complete', 'comments')