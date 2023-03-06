from rest_framework import serializers
from .models import Address


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "city", "street", "number", "zip_code", "state"]
