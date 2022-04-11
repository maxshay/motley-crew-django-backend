from rest_framework import permissions

# for general purpose, if has field 'owner'
class IsOwner(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    # Write permissions are only allowed to the owner of the snippet.
    return obj.owner == request.user


# for individual route items
class IsAssignee(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    # Write permissions are only allowed to the owner of the snippet.
    return obj.assignee == request.user


# for route slips
class IsShared(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    # Write permissions are only allowed to the owner of the snippet.
    # TODO: make this work, syntax is not correct
    return request.user in obj.shared