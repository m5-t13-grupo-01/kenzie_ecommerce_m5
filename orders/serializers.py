from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "created_at",
            "updated_at"
        ]
        read_only = ["id", "created_at", "updated_at"]