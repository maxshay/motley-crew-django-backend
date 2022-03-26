from django.db import models
from folders.models import Folder
from users.models import User

class RouteSlip(models.Model):
  
  class OrderTypes(models.TextChoices):
    IN_ORDER = 'in_order'
    PARALLEL = 'parallel'
    BOTH = 'both'

  
  folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='routeSlips')
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  complete = models.BooleanField(default=False)
  order_type = models.CharField(max_length=16, choices=OrderTypes.choices, null=True)
  current_id = models.IntegerField(null=True)
  is_archived = models.BooleanField(default=False)


