from rest_framework import serializers
from .models import User

# new
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PartialUserSerializer(serializers.ModelSerializer):
  firstName = serializers.CharField(source='first_name', read_only=True)
  lastName = serializers.CharField(source='last_name', read_only=True)
  fullName = serializers.SerializerMethodField('get_user_full_name', read_only=True)
  profileImage = serializers.CharField(source='profile_image')

  def get_user_full_name(self, obj):
    # print(obj.first_name, obj.last_name)
    # request = self.context['request']
    # user = request.user
    name = obj.first_name + " " + obj.last_name
    return name

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'firstName', 'lastName', 'fullName', 'profileImage')




class AssigneeSerializer(serializers.ModelSerializer):
  firstName = serializers.CharField(source='first_name', read_only=True)
  lastName = serializers.CharField(source='last_name', read_only=True)
  fullName = serializers.SerializerMethodField('get_user_full_name', read_only=True)
  profileImage = serializers.CharField(source='profile_image')

  def get_user_full_name(self, obj):
    # print(obj.first_name, obj.last_name)
    # request = self.context['request']
    # user = request.user
    name = obj.first_name + " " + obj.last_name
    return name

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'firstName', 'lastName', 'fullName', 'profileImage')
 

class UserSerializer(serializers.ModelSerializer):
  firstName = serializers.CharField(source='first_name', read_only=True)
  lastName = serializers.CharField(source='last_name', read_only=True)
  profileImage = serializers.CharField(source='profile_image')

  fullName = serializers.SerializerMethodField('get_user_full_name', read_only=True)

  dateJoined = serializers.DateTimeField(source='date_joined', read_only=True)
  lastLogin = serializers.DateTimeField(source='last_login', read_only=True)
  isActive = serializers.BooleanField(source='is_active', read_only=True)
  isStaff = serializers.BooleanField(source='is_staff', read_only=True)
  isSuperuser = serializers.BooleanField(source='is_superuser', read_only=True)

  managerId = serializers.IntegerField(source='manager_id', read_only=True)

  def get_user_full_name(self, obj):
    # print(obj.first_name, obj.last_name)
    # request = self.context['request']
    # user = request.user
    name = obj.first_name + " " + obj.last_name
    return name

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'firstName', 'lastName', 'fullName', 'dateJoined', 'lastLogin', 'isActive', 'isStaff', 'isSuperuser', 'profileImage', 'managerId')
    extra_kwargs = {
      'username': {'read_only': True}
    }

  # def create(self, validated_data):
  #   full_name = validated_data.get('full_name')
  #   validated_data['username'] = fullname + '#dcf' // whatever logic you want to use here
  #   return super(RegisterSerializer, self).create(validated_data)
  #   # or 
  #   # return HNUsers.objects.create(**validated_data)

class LogInSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    user_data = UserSerializer(user).data
    for key, value in user_data.items():
      if key != 'id':
        token[key] = value
    return token