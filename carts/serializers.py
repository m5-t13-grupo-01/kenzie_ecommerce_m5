from rest_framework import serializers
from .models import Cart
from products.models import CartProducts, Product


class CartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, instance: Cart):
        products_obj = CartProducts.objects.filter(cart=instance)
        products_ids = [str(product.product_id) for product in products_obj]
        products = []

        if products_ids:
            for product_id in products_ids:
                product = Product.objects.filter(pk=product_id).first()

                products.append(
                    {
                        "name": product.name,
                        "price": product.price,
                    }
                )

        return products

    class Meta:
        model = Cart
        fields = ["id", "products"]
        read_only_fields = ["id", "products"]
