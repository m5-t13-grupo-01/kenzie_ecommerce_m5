from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "city",
            "street",
            "number",
            "zip_code",
            "state",
        ]
        read_only_fields = ["id"]
