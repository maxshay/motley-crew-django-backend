from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class UserAdminCreationForm(UserCreationForm):
  extra_field = forms.CharField(required=True)
  class Meta:
    model = User
    fields = ('username' , 'extra_field', 'email', 'is_active')


class UserAdminChangeForm(UserChangeForm):

  class Meta:
    model = User
    fields = ('email', 'username')