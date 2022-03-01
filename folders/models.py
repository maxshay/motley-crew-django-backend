from django.db import models
from users.models import User

class Folder(models.Model):
  name = models.CharField(max_length=255)

  # belongs to User
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('owner', 'name')

  def __str__(self):
    return f'{self.name}, id: {self.id}'