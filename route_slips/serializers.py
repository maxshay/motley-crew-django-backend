from rest_framework import serializers
from .models import RouteSlip


class RouteSlipSerializer(serializers.ModelSerializer):

  class Meta:
    model = RouteSlip
    fields = '__all__'
    # exclude = ['model_a_field', ']