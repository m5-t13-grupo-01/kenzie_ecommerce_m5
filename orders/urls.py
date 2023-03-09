from django.urls import path
from .views import CreateOrderView, UpdateOrderView, GetOrdersView


urlpatterns = [
    path("orders/", CreateOrderView.as_view()),
    path("orders/report/", GetOrdersView.as_view()),
    path("orders/<str:order_id>/", UpdateOrderView.as_view()),
]
