from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

# TODO: add username to user create form

# new fields for add user do not work
class UserAdminCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email',)


class UserAdminChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = ('email', 'username', 'is_staff', 'is_active')