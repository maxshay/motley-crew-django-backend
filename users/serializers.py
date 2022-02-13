from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  firstName = serializers.CharField(source='first_name')
  lastName = serializers.CharField(source='last_name')
  dateJoined = serializers.DateTimeField(source='date_joined')
  lastLogin = serializers.DateTimeField(source='last_login')
  isActive = serializers.BooleanField(source='is_active')
  isStaff = serializers.BooleanField(source='is_staff')
  isSuperuser = serializers.BooleanField(source='is_superuser')

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'firstName', 'lastName', 'dateJoined', 'lastLogin', 'isActive', 'isStaff', 'isSuperuser')