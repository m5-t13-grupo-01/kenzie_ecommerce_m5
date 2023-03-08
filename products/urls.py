from django.urls import path
from .views import ProductView, ProductDetailView, AddProductToCart

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<str:product_id>/", ProductDetailView.as_view()),
    path("products/<str:product_id>/cart/", AddProductToCart.as_view()),
]
