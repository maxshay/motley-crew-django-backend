from rest_framework import serializers
from .models import File

# models
from folders.models import Folder as FolderModel

# serializers
from folders.serializers import FolderSerializer
from users.serializers import UserSerializer

class FileSerializer(serializers.ModelSerializer):

  owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
  )

  class Meta:
    model = File
    fields = ('id', 'parent_folder', 'name', 'owner', 'file')


class CreateFileSerializer(serializers.ModelSerializer):
  owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
  )

  class Meta:
    model = File
    fields = ('id', 'parent_folder', 'name', 'owner', 'file')
    read_only_fields = ('parent_folder',)
