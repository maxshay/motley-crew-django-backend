from rest_framework import serializers
from .models import User

# new
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
  firstName = serializers.CharField(source='first_name', read_only=True)
  lastName = serializers.CharField(source='last_name', read_only=True)
  profileImage = serializers.CharField(source='profile_image')
  dateJoined = serializers.DateTimeField(source='date_joined', read_only=True)
  lastLogin = serializers.DateTimeField(source='last_login', read_only=True)
  isActive = serializers.BooleanField(source='is_active', read_only=True)
  isStaff = serializers.BooleanField(source='is_staff', read_only=True)
  isSuperuser = serializers.BooleanField(source='is_superuser', read_only=True)

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'firstName', 'lastName', 'dateJoined', 'lastLogin', 'isActive', 'isStaff', 'isSuperuser', 'profileImage')
    extra_kwargs = {
      'username': {'read_only': True}
    }

class LogInSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    user_data = UserSerializer(user).data
    for key, value in user_data.items():
      if key != 'id':
        token[key] = value
    return token