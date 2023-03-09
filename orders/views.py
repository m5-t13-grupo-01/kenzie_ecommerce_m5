from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from .models import Order
from .serializers import OrderReturnSerializer, OrderUpdateSerializer, OrderSerializer
from .mixins import ProductIsAvailableMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSellerOrAdmin, IsAdminOrSeller


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


class GetOrdersView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSeller]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_seller and self.request.query_params.get("status"):
            return Order.objects.filter(
                seller_id=self.request.user.id,
                status=self.request.query_params["status"],
            )

        if self.request.user.is_seller:
            return Order.objects.filter(seller_id=self.request.user.id)

        return Order.objects.all()


class GetUserOrdersView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
