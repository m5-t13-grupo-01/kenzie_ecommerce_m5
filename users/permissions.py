from rest_framework import permissions
from rest_framework.views import View, Request
from .models import User


class IsAdminJustForGetList(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.method == "POST" or (
            request.method in permissions.SAFE_METHODS
            and request.user.is_authenticated
            and request.user.is_superuser
        )


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_admin
        )
