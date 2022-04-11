from datetime import datetime
from django.db import models

from users.models import User

class Folder(models.Model):
  name = models.CharField(max_length=255)

  description = models.CharField(max_length=255, null=True)
  color = models.CharField(max_length=16, null=True)

  # TODO: make this required, not automatic default
  desired_completion_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
  expedited = models.BooleanField(default=False)
  confidential = models.BooleanField(default=False)

  # belongs to User
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  current_active_route = models.IntegerField(null=True)

  class Meta:
    unique_together = ('owner', 'name')

  def __str__(self):
    return f'{self.name}, id: {self.id}'