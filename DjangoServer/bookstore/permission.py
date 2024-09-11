from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to allow only admins to access certain views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class IsClient(BasePermission):
    """
    Custom permission to allow only clients to access certain views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'client'