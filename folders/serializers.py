from rest_framework import serializers
from .models import Folder

from route_slips.models import RouteSlip
from route_slips.serializers import CreateRouteSlipSerializer, RouteSlipSerializer

class FolderSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.DateTimeField(source='desired_completion_date', read_only=True)
  routeSlips = RouteSlipSerializer(source='routeslip_set', many=True)

  class Meta:
    model = Folder
    fields = ('id', 'name', 'description', 'color', 'expedited', 'confidential', 'owner', 'desiredCompletionDate', 'routeSlips')
  

class CreateFolderSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.DateTimeField(source='desired_completion_date')
  owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
  )
 
  def create(self, validated_data):
    folder_instance = Folder.objects.create(**validated_data)
    print(' > PASSED FOLDER')
    # create empty route slip here
    body = {'folder_id': folder_instance.id, 'owner': folder_instance.owner.id, 'order_type': 'IN_ORDER'}
    ri = CreateRouteSlipSerializer(data=body)
    ri.is_valid(raise_exception=True)
    ri.save()
    return folder_instance

  class Meta:
    model = Folder
    fields = ('id', 'name', 'description', 'color', 'desiredCompletionDate', 'expedited', 'confidential', 'owner')
