from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from .serializers import UserRegisterSerializer
from .permissions import IsBuyer, IsSeller

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class BuyerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsBuyer]

    def get(self, request):
        return Response({"message": f"Welcome Buyer {request.user.username}!"})

class SellerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsSeller]

    def get(self, request):
        return Response({"message": f"Welcome Seller {request.user.username}!"})
