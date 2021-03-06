from datetime import datetime
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from motleycrew_backend.permissions import IsOwner

from .models import Message as MessageModel
from route_slips.models import RouteSlip as RouteSlipModel

from .serializers import MessageSerializer

# Create your views here.
class Message(generics.RetrieveDestroyAPIView):
  permission_classes = (IsOwner,)
  queryset = MessageModel.objects.all()
  serializer_class = MessageSerializer
  lookup_field = 'id'


class Messages(generics.ListAPIView):
  serializer_class = MessageSerializer

  def get_queryset(self):
    user = self.request.user
    return MessageModel.objects.filter(owner=user)


class Notifications(APIView):
  def get(self, request, format=None):
    user = request.user
    messages = MessageModel.objects.filter(owner=user)
    count = 0
    for m in messages:
      if m.read is False:
        count+=1
    return Response({'count': count})


class ReadMessage(APIView):
  permission_classes = (IsOwner,)
  serializer_class = MessageSerializer

  def put(self, request, id):
    message = get_object_or_404(MessageModel, id=id)
    self.check_object_permissions(self.request, message)

    if message.read == False:
      message.read = True
      message.read_at = datetime.now()
      message.save()

    message_serialized = MessageSerializer(message)
    return Response(message_serialized.data)