import uuid
from datetime import datetime
from django.db import models

from users.models import User

# Create your models here.
class Message(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  message_type = models.CharField(max_length=16) # notification, alert?, reminder?
  contents = models.CharField(max_length=255)
  read = models.BooleanField(default=False)
  read_at = models.DateTimeField(null=True, blank=True)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)