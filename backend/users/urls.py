from django.urls import path
from .views import (
    UserRegisterView,
    CustomLoginView,
    CustomLogoutView,
    BuyerDashboardView,
    SellerDashboardView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('buyer/dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('seller/dashboard/', SellerDashboardView.as_view(), name='seller_dashboard'),
]
