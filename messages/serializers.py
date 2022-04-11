from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
  messageType = serializers.CharField(source='message_type')
  readAt = serializers.CharField(source='read_at')
  createdAt = serializers.CharField(source='created_at')

  class Meta:
    model = Message
    exclude = ('message_type', 'read_at', 'created_at',)


class MessageListSerializer(serializers.ModelSerializer):
  messageType = serializers.CharField(source='message_type')

  pass


class CreateMessageSerializer(serializers.ModelSerializer):
  pass