import uuid
from django.db import models

from users.models import User
from route_slips.models import RouteSlip
from files.models import File

# Create your models here.
class RouteItem(models.Model):
  ACTION_TYPE_CHIOCES = [
    ('VIEW', 'view'),
    ('SIGN', 'sign'),
    ('OTHER', 'other'),
  ]

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  route_slip_id = models.ForeignKey(RouteSlip, on_delete=models.CASCADE)
  assignee = models.ForeignKey(User, on_delete=models.CASCADE)
  action_type = models.CharField(max_length=8, choices=ACTION_TYPE_CHIOCES, default='VIEW')
  order_num = models.SmallIntegerField(null=True)
  complete = models.BooleanField(default=False)
  completed_at = models.DateTimeField(null=True, blank=True)
  comments = models.CharField(max_length=255, null=True)

  # image_ref
  # image_step
  file = models.ForeignKey(File, on_delete=models.CASCADE, null=True)

  # coord ref
  # add this
  # form_field = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
