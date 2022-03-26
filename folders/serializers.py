from rest_framework import serializers
from .models import Folder

from route_slips.models import RouteSlip
from route_slips.serializers import RouteSlipSerializer, ActiveRouteSlipSerializer

class FolderSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.DateTimeField(source='desired_completion_date')
  routeSlips = ActiveRouteSlipSerializer(many=True)
 
  class Meta:
    model = Folder
    fields = ('id', 'name', 'description', 'color', 'desiredCompletionDate', 'expedited', 'confidential', 'owner', 'routeSlips')


class CreateFolderSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.DateTimeField(source='desired_completion_date')
  owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
  )
  """
  def create(self, validated_data):
    # return Snippet.objects.create(**validated_data)
    group_data = validated_data.pop('group')
    group, _ = Group.objects.get_or_create(name=group_data)
    data = {
      key: value for key, value in validated_data.items()
      if key not in ('password1', 'password2')
    }
    data['password'] = validated_data['password1']
    user = self.Meta.model.objects.create_user(**data)
    user.groups.add(group)
    user.save()
    return user
  """
  def create(self, validated_data):
    folder_instance = Folder.objects.create(**validated_data)
    # create empty route slip here
    RouteSlip.objects.create(folder_id=folder_instance, owner=folder_instance.owner)
    return folder_instance

  class Meta:
    model = Folder
    fields = ('id', 'name', 'description', 'color', 'desiredCompletionDate', 'expedited', 'confidential', 'owner')
