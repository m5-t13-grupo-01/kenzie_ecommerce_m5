from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserView, UserDetailView, ListUserCartView

urlpatterns = [
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<str:user_id>/", UserDetailView.as_view()),
    path("users/cart/products/", ListUserCartView.as_view()),
]
