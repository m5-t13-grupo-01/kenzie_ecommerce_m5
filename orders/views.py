from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Order
from .serializers import OrderReturnSerializer, OrderUpdateSerializer
from .mixins import ProductIsAvailableMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSellerOrAdmin


class CreateOrderView(ProductIsAvailableMixin, CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderReturnSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateOrderView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSellerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer

    lookup_url_kwarg = "order_id"
