from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsSeniorStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        # if request.user.is_anonymous:
        #     return False
        return request.user.position in ('director', 'supervisor', 'middle_manager')
