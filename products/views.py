from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from .models import Product, CartProducts
from .serializers import ProductSerializer, AddProductCartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsSellerOrAdmin
from users.permissions import IsOwnerOrAdmin
from django.shortcuts import get_object_or_404
from carts.models import Cart


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.request.query_params.get("name"):
            return Product.objects.filter(name=self.request.query_params["name"])

        if self.request.query_params.get("id"):
            return Product.objects.filter(id=self.request.query_params["id"])

        if self.request.query_params.get("category"):
            return Product.objects.filter(
                category=self.request.query_params["category"]
            )

        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"


class AddProductToCart(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = CartProducts.objects.all()
    serializer_class = AddProductCartSerializer

    def perform_create(self, serializer):
        product_selected = get_object_or_404(Product, id=self.kwargs["product_id"])
        cart_selected = get_object_or_404(Cart, id=self.request.user.cart.id)
        return serializer.save(product=product_selected, cart=cart_selected)
