from rest_framework import serializers
from .models import User

# new
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class LogInSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    user_data = UserSerializer(user).data
    for key, value in user_data.items():
      if key != 'id':
        token[key] = value
    return token