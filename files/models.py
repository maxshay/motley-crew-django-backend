from django.db import models
from folders.models import Folder
from users.models import User

# https://stackoverflow.com/questions/9736548/database-schema-how-the-relationship-can-be-designed-between-user-file-and-fol
# https://docs.djangoproject.com/en/4.0/ref/models/fields/

class File(models.Model):
  name = models.CharField(max_length=255)
  # parent folder
  # url = models

  # belongs to: Folder
  parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

  # belongs to: User
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  class Meta:
    unique_together = ('parent_folder', 'name')