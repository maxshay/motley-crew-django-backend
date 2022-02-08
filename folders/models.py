from django.db import models
from users.models import User

class Folder(models.Model):
  name = models.CharField(max_length=255)
  # type?
  # shared?

  # belongs to User
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('user', 'name')
