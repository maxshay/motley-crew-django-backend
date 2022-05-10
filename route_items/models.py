import uuid
from django.db import models

from users.models import User
from route_slips.models import RouteSlip
from files.models import File

class RouteItem(models.Model):
  ACTION_TYPE_CHIOCES = (
    ('VIEW', 'view'),
    ('SIGN', 'sign'),
    ('OTHER', 'other'),
  )
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  action_type = models.CharField(max_length=8, choices=ACTION_TYPE_CHIOCES)
  order_num = models.SmallIntegerField(null=True, blank=True)
  comments = models.CharField(max_length=255, null=True)

  complete = models.BooleanField(default=False)
  completed_at = models.DateTimeField(null=True, default=None)

  # route slip has many route items
  route_slip = models.ForeignKey(RouteSlip, on_delete=models.CASCADE, null=True)

  # file has a route item
  file = models.ForeignKey(File, on_delete=models.CASCADE, null=True)

  # assignee has many route items
  assignee = models.ForeignKey(User, on_delete=models.CASCADE)