from django.urls import path
from .views import HomeView, ProductsView



urlpatterns = [
    path('',ProductsView.as_view(), name='home')
]