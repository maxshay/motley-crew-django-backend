from rest_framework import serializers
from .models import Message

from users.serializers import UserSerializer
from files.serializers import FileSerializer
from route_items.serializers import RouteItemSerializer

class MessageSerializer(serializers.ModelSerializer):
  messageType = serializers.CharField(source='message_type')
  readAt = serializers.CharField(source='read_at')
  createdAt = serializers.CharField(source='created_at')
  routeItem = RouteItemSerializer(source='route_item')

  class Meta:
    model = Message
    fields = ('id', 'messageType', 'contents', 'read', 'readAt', 'createdAt', 'routeItem')


class MessageListSerializer(serializers.ModelSerializer):
  messageType = serializers.CharField(source='message_type')
  pass


class CreateMessageSerializer(serializers.ModelSerializer):

  class Meta:
    model = Message
    fields = '__all__'
