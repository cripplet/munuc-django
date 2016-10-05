from rest_framework import permissions

from django.core import exceptions

from django.contrib.auth.models import Group


class CommitteeStafferPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    try:
      group = Group.objects.get(name='committee_staffer')
    except exceptions.ObjectDoesNotExist:
      return False
    return group in request.user.groups.all()
