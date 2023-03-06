from rest_framework import permissions
from rest_framework.views import View, Request


class IsAdminJustForGetList(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.method == "POST" or (
            request.method in permissions.SAFE_METHODS
            and request.user.is_authenticated
            and request.user.is_superuser
        )
