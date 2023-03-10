from rest_framework import permissions
from rest_framework.views import View, Request
from .models import Order


class IsSellerOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Order):
        return (
            request.user.is_authenticated
            and obj.seller_id == request.user.id
            and request.user.is_seller
            or request.user.is_admin
        )


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.user.is_authenticated
            and request.user.is_admin
            or request.user.is_seller
        )
