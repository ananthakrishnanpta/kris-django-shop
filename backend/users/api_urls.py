from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import (
    RegisterAPIView,
    BuyerDashboardAPIView,
    SellerDashboardAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('buyer/dashboard/', BuyerDashboardAPIView.as_view(), name='api_buyer_dashboard'),
    path('seller/dashboard/', SellerDashboardAPIView.as_view(), name='api_seller_dashboard'),
]
