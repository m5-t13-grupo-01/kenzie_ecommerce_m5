from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import Request, View
from .models import Product


class IsSellerOrAdmin(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Product):
        if request.method == "DELETE" or request.method == "PATCH":
            return request.user.id == obj.seller.id or request.user.is_admin
        else:
            return (
                request.method in SAFE_METHODS
                or request.user.is_superuser
                or request.user.is_seller
            )
