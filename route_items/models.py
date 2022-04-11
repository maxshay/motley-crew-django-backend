import uuid
from django.db import models

from users.models import User
from route_slips.models import RouteSlip

# Create your models here.
class RouteItem(models.Model):
  ACTION_TYPE_CHIOCES = [
    ('VIEW', 'view'),
    ('SIGN', 'sign'),
    ('OTHER', 'other'),
  ]

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  # route_slip_id - route slip ref
  route_slip_id = models.ForeignKey(RouteSlip, on_delete=models.CASCADE)

  # person (assignee) - user model ref
  assignee = models.ForeignKey(User, on_delete=models.CASCADE)

  # type - string (view, sign)
  action_type = models.CharField(max_length=8, choices=ACTION_TYPE_CHIOCES, default='VIEW')

  # order_num - integer
  order_num = models.SmallIntegerField(null=True)

  # complete - boolean
  complete = models.BooleanField(default=False)

  # datetime complete
  completed_at = models.DateTimeField(null=True, blank=True)

  # comments - string
  comments = models.CharField(max_length=255, null=True)
