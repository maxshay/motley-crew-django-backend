from rest_framework import serializers
from .models import RouteItem


# from users.models import User
from users.serializers import AssigneeSerializer
from files.serializers import FileInRouteItemSerializer
from form_fields.serializers import FormFieldSerializer


class SortedRouteItemSerializer(serializers.ListSerializer):
  def to_representation(self, data):
    # data = data.filter(is_archived=False)
    return super(SortedRouteItemSerializer, self).to_representation(data)


# get One
class RouteItemSerializer(serializers.ModelSerializer):
  actionType = serializers.CharField(source='action_type')
  orderNum = serializers.IntegerField(source='order_num')
  completedAt = serializers.DateTimeField(source='completed_at')
  formFields = FormFieldSerializer(source='formfield_set', many=True)
  assignee = AssigneeSerializer()
  file = FileInRouteItemSerializer()

  # form field(s)

  class Meta:
    model = RouteItem
    fields = ('id', 'assignee', 'actionType', 'orderNum', 'complete', 'comments', 'completedAt', 'file', 'formFields')


def validate_action_type(value):
  """
  Check actionType is valid choice
  """
  if value not in ['view', 'sign', 'other']:
    raise serializers.ValidationError({'actionType': 'Invalid field type. Must be either \'view\', \'sign\', or \'other\''})

class CreateRouteItemSerializer(serializers.ModelSerializer):
  actionType = serializers.CharField(source='action_type', validators=[validate_action_type])
  orderNum = serializers.IntegerField(source='order_num', required=False)


  class Meta:
    model = RouteItem
    fields = ('id', 'assignee', 'actionType', 'orderNum', 'complete', 'comments', 'route_slip_id', 'file', 'assignee')