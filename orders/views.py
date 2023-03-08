from rest_framework.generics import CreateAPIView
from .models import Order
from .serializers import OrderReturnSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CreateOrderView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderReturnSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
