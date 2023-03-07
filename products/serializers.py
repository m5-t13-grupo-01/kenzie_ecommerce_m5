from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "stock",
            "seller",
            "carts",
            "is_available",
        ]
        read_only_fields = ["id", "seller", "carts"]
        extra_kwargs = {
            "is_available": {
                "write_only": True,
            }
        }
