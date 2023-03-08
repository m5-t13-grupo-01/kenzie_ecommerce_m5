from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=127)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True, null=True)

    seller = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )

    carts = models.ManyToManyField(
        "carts.Cart",
        through="CartProducts",
        related_name="products",
    )


class CartProducts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    cart = models.ForeignKey(
        "carts.Cart", on_delete=models.CASCADE, related_name="cart_products"
    )

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="cart_products"
    )
