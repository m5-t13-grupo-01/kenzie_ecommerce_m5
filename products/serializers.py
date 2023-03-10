from rest_framework import serializers
from .models import Product, CartProducts


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
        ]
        read_only_fields = ["seller"]

    def update(self, instance: Product, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        if instance.stock <= 0:
            instance.is_available = False
        else:
            instance.is_available = True

        instance.save()
        return Product.objects.filter(pk=instance.id).first()


class AddProductCartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartProducts
        fields = ["id", "cart", "product"]
        read_only_fields = ["id", "cart", "product"]
