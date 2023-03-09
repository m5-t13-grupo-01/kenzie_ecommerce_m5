from django.urls import path
from .views import CreateOrderView, UpdateOrderView


urlpatterns = [
    path("orders/", CreateOrderView.as_view()),
    path("orders/<str:order_id>/", UpdateOrderView.as_view()),
]
