import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

from files.models import File

# Create your models here.
class FormField(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  page_num = models.SmallIntegerField(default=0)
  width = models.SmallIntegerField(default=0)
  height = models.SmallIntegerField(default=0)
  xpos = models.SmallIntegerField(default=0)
  ypos = models.SmallIntegerField(default=0)
  dimensions = ArrayField(models.IntegerField(), size=6, null=True)

  # belongs to file
  file = models.ForeignKey(File, on_delete=models.CASCADE)