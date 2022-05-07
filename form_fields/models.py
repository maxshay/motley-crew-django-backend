import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

from files.models import File
from route_items.models import RouteItem

# Create your models here.
class FormField(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  # possible values are: 'sign', 'date', 'check'
  form_type = models.CharField(max_length=8)
  page_num = models.SmallIntegerField()
  width = models.SmallIntegerField()
  height = models.SmallIntegerField()
  xpos = models.SmallIntegerField()
  ypos = models.SmallIntegerField()
  # dimensions = ArrayField(models.IntegerField(), size=6, null=True)

  # file has many form fields
  file = models.ForeignKey(File, on_delete=models.CASCADE)

  # route item has many form fields
  route_item = models.ForeignKey(RouteItem, on_delete=models.CASCADE)