from django.db import models
from folders.models import Folder
from users.models import User
# from django.contrib.postgres.fields import ArrayField

# https://stackoverflow.com/questions/9736548/database-schema-how-the-relationship-can-be-designed-between-user-file-and-fol
# https://docs.djangoproject.com/en/4.0/ref/models/fields/


def _generate_dummy_fields():
  return [[ 0, 1, 538, 241, 21, 23]
          [ 0, 1, 167, 242, 20, 22]
          [ 0, 1, 189, 242, 17, 22]
          [ 0, 1, 208, 242, 23, 24]
          [ 0, 1, 233, 242, 18, 23]
          [ 0, 1, 255, 242, 17, 22]]

class FormField(models.Model):
  pass


class File(models.Model):
  name = models.CharField(max_length=255, blank=True)
  file = models.FileField(null=True, upload_to='files')

  # belongs to: Folder
  parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

  # belongs to: User
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  # form_fields = models.ForeignKey(FormField, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

  class Meta:
    unique_together = ('parent_folder', 'name')