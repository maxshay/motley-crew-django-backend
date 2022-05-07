from rest_framework import serializers
from django.db import IntegrityError
from .models import File

# models
from folders.models import Folder as FolderModel

# serializers
from users.serializers import UserSerializer, PartialUserSerializer
from form_fields.serializers import FormFieldSerializer

class FileSerializer(serializers.ModelSerializer):
  parentFolder = serializers.PrimaryKeyRelatedField(source='parent_folder', read_only=True)
  formFields = FormFieldSerializer(source='formfield_set', many=True)
  class Meta:
    model = File
    fields = ('id', 'parentFolder', 'name', 'file', 'owner', 'formFields')


class FileInRouteItemSerializer(serializers.ModelSerializer):
  parentFolder = serializers.PrimaryKeyRelatedField(source='parent_folder', read_only=True)

  class Meta:
    model = File
    fields = ('id', 'parentFolder', 'name', 'file', 'owner')


class FilesSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.DateTimeField(source='desired_completion_date')
  files = FileSerializer(source='file_set', many=True)
  owner = PartialUserSerializer()

  class Meta:
    model = FolderModel
    fields = ('id', 'name', 'description', 'color', 'desiredCompletionDate', 'expedited', 'confidential', 'owner', 'files')
    # depth = 1


# TODO: file name to model name
# TODO: file type checking
class CreateFileSerializer(serializers.ModelSerializer):
  owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
  )
  parentFolder = serializers.PrimaryKeyRelatedField(source='parent_folder', read_only=True)

  def create(self, validated_data):
    try:
      # validated_data['user'] = self.context['request'].user
      # print(' > context:', self.context['request']).user
      f = self.context['request'].FILES
      print(' > name', f['file'].name)
      validated_data['name'] = f['file'].name
      print(validated_data)
      # raise IntegrityError('Test error')
      return super().create(validated_data)
    except IntegrityError as e:
      error_msg = {'message': e}
      print(' > ', e)
      raise serializers.ValidationError(error_msg)

  class Meta:
    model = File
    fields = ('id', 'parentFolder', 'name', 'owner', 'file')
    read_only_fields = ('parentFolder',)
