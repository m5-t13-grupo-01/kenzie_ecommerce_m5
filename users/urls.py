from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserView, UserDetailView

urlpatterns = [
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/", UserView.as_view()),
    path("users/<str:user_id>/", UserDetailView.as_view()),
]
