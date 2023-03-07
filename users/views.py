from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminJustForGetList, IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminJustForGetList]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
