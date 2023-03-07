from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsSellerOrAdmin


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
