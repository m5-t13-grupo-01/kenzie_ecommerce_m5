from .utils import isAvailableProduct, NotAvailableException
from products.models import Product, CartProducts
from rest_framework.response import Response


class ProductIsAvailableMixin:
    def post(self, request, *args, **kwargs):
        products = CartProducts.objects.filter(cart=request.user.cart.id)

        for product in products:
            pro = Product.objects.filter(pk=product.product_id).first()

            try:
                isAvailableProduct(pro)
            except NotAvailableException as err:
                return Response({"detail": err.message}, status=400)

        return self.create(request, *args, **kwargs)
