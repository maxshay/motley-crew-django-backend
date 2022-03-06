from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.
class User(AbstractUser):
  is_active = models.BooleanField(default=True)
  # profile_image = models.TextField(())

  objects = UserManager()

  def __str__(self):
    return self.username
