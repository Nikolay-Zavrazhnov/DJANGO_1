from rest_framework import response
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.user.is_superuser is True:
            return True
        else:
            return request.user == obj.creator
