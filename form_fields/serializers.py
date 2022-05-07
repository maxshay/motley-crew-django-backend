

from rest_framework import serializers
from .models import FormField as FormFieldModel

class FormFieldSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = FormFieldModel
    fields = '__all__'