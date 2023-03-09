from rest_framework import serializers
from .models import Order
from products.models import Product, CartProducts
from users.mailer import send_email


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, instance: Order):
        products_ids = instance.products.split(",")
        products = []

        for product_id in products_ids:
            product = Product.objects.filter(pk=product_id).first()
            products.append(
                {
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "category": product.category,
                }
            )

        return products

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
            "products",
        ]
        read_only = ["id", "created_at", "updated_at"]


class OrderReturnSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    def create(self, validated_data):
        my_products = CartProducts.objects.filter(cart=validated_data["user"].cart.id)

        products_for_seller = {}

        for product in my_products:
            pro = Product.objects.filter(pk=product.product_id).first()

            if pro.stock > 0:
                pro.stock -= 1

            if pro.stock == 0:
                pro.is_available = False

            pro.save()

            if pro.seller not in products_for_seller:
                products_for_seller[pro.seller] = [pro]
            else:
                products_for_seller[pro.seller].append(pro)

        orders = []

        for value in products_for_seller.values():
            products = []

            for obj in value:
                products.append(str(obj.id))

            products = ",".join(products)

            order = Order.objects.create(products=products, user=validated_data["user"])
            orders.append(order)

        return {"orders": orders}

    class Meta:
        model = Order
        fields = ["orders"]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only = ["id", "created_at", "updated_at"]

    def update(self, instance: Order, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        send_email(
            destiny=instance.user.email,
            message=f"O status do seu pedido foi atualizado para {instance.status}",
            title=f"Atualização do Pedido - {instance.id}",
        )
        return instance
