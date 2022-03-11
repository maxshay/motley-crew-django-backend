from rest_framework import serializers
from .models import RouteSlip


class RouteSlipSerializer(serializers.ModelSerializer):

  # owner = serializers.HiddenField(
  #   default=serializers.CurrentUserDefault()
  # )

  class Meta:
    model = RouteSlip
    fields = '__all__'
    # exclude = ['model_a_field', ']