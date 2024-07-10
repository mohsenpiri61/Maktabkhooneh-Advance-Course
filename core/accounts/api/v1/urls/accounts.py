from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    # path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
    path('token/login/', views.CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    path("test-email", views.TestEmailSend.as_view(), name="test-email"),
    # change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name="change-password"),
    
    
    # login jwt
    # path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name="jwt-refresh"),
    path('jwt/verify/', TokenVerifyView.as_view(), name="jwt-verify"),
    
    # custom jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    
]
