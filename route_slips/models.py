import json
import uuid
from django.db import models
from folders.models import Folder
from users.models import User

class RouteSlip(models.Model):
  ORDERING_TYPE_CHIOCES = [
    ('IN_ORDER', 'inorder'),
    ('PARALLEL', 'parallel'),
    ('BOTH', 'both'),
  ]

  folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='routeSlips')
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  complete = models.BooleanField(default=False)
  order_type = models.CharField(max_length=16, choices=ORDERING_TYPE_CHIOCES, default='IN_ORDER', blank=True)
  current_route_item_id = models.IntegerField(null=True)
  is_archived = models.BooleanField(default=False)
  shared_with = models.JSONField(default=list)
  slug = models.UUIDField(default=uuid.uuid4, editable=False)

  route_start_time = models.DateTimeField(null=True, blank=True)
  # TODO: route_restarted?


