from django.urls import path
from .views import (
    ProductView,
    ProductDetailView,
    AddProductToCart,
    RemoveProductCartView,
)

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<str:product_id>/", ProductDetailView.as_view()),
    path("products/<str:product_id>/cart/", AddProductToCart.as_view()),
    path("cart/product/remove/<str:product_id>/", RemoveProductCartView.as_view()),
]
