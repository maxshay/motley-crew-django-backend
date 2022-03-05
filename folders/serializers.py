from rest_framework import serializers
from .models import Folder

class FolderSerializer(serializers.ModelSerializer):
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
  
  class Meta:
    model = Folder
    fields = ('id', 'name', 'description', 'color', 'desiredCompletionDate', 'expedited', 'confidential', 'owner')
