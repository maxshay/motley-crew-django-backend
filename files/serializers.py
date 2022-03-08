from rest_framework import serializers
from .models import File

# models
from folders.models import Folder as FolderModel

# serializers
from folders.serializers import FolderSerializer
from users.serializers import UserSerializer

class FileSerializer(serializers.ModelSerializer):
  parentFolder = serializers.PrimaryKeyRelatedField(source='parent_folder', read_only=True)

  class Meta:
    model = File
    fields = ('id', 'parentFolder', 'name', 'file', 'owner')




class FilesSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.DateTimeField(source='desired_completion_date')
  files = FileSerializer(source='file_set', many=True)

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


  class Meta:
    model = File
    fields = ('id', 'parentFolder', 'name', 'owner', 'file')
    read_only_fields = ('parentFolder',)
