from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

from .models import User

# TODO: add username to user create form

class UserAdmin(BaseUserAdmin):
  # The forms to add and change user instances
  form = UserAdminChangeForm
  add_form = UserAdminCreationForm
  model = User

  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserAdmin
  # that reference specific fields on auth.User.
  list_display = ('username', 'id', 'email', 'is_staff', 'is_active', 'is_superuser')
  list_filter = ('is_staff', 'is_active',)
  fieldsets = (
    (None, {'fields': ('email', 'username', 'password')}),
    ('Personal info', {'fields': ()}),
    ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
    ),
  )
  search_fields = ('email',)
  ordering = ('email',)
  filter_horizontal = ()


admin.site.register(User, UserAdmin)