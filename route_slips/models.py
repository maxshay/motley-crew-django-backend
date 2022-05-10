import json
import uuid
from django.db import models
from folders.models import Folder
from users.models import User
from django.contrib.postgres.fields import ArrayField

class RouteSlip(models.Model):
  ORDERING_TYPE_CHIOCES = [
    ('IN_ORDER', 'inorder'),
    ('PARALLEL', 'parallel'),
    ('BOTH', 'both'),
  ]

  # id
  complete = models.BooleanField(default=False)
  order_type = models.CharField(max_length=16, choices=ORDERING_TYPE_CHIOCES, default='IN_ORDER')
  is_archived = models.BooleanField(default=False)
  route_start_time = models.DateTimeField(null=True)

  current_route_item = models.UUIDField(null=True) # the id of the route item the route is currently on
  route_items_queue = ArrayField(models.UUIDField(), default=list)

  # belongs to a Folder
  folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE)

  # belongs to a User
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

# psycopg2.errors.NotNullViolation: null value in column "owner_id"    of relation "folders_folder"        violates not-null constraint
# psycopg2.errors.NotNullViolation: null value in column "route_items" of relation "route_slips_routeslip" violates not-null constraint

'''
from route_items.models import RouteItem
from folders.models import Folder
from users.models import User
from route_slips.models import RouteSlip

f = Folder.objects.get(id=60)
u = User.objects.get(id=4)
rs = RouteSlip.objects.create(folder_id=f,owner=u)



'''