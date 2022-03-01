from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
  parentFolder = serializers.IntegerField(source='parent_folder.id')

  class Meta:
    model = File
    fields = ('id', 'parentFolder', 'name', 'owner', 'file')