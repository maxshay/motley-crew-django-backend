from django.db import models


# https://stackoverflow.com/questions/9736548/database-schema-how-the-relationship-can-be-designed-between-user-file-and-fol
# https://docs.djangoproject.com/en/4.0/ref/models/fields/

# class User():
  # id:
  # first_name:
  # last_name:
  # ...

  # has one or many folders



# class Folder():
  # name
  # parent folder
  # root?
  # type?
  # shared?


  # belongs to User



class File():
  # name
  # parent folder
  # url

  # belongs to: Folder
  

  def __str__:
    return self.filename