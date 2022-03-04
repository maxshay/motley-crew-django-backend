from rest_framework import serializers
from .models import Folder

class FolderSerializer(serializers.ModelSerializer):
  desiredCompletionDate = serializers.BooleanField(source='desired_completion_date')

  class Meta:
    model = Folder
    fields = ('name', 'description', 'color', 'desiredCompletionDate', 'expedited', 'confidential')
