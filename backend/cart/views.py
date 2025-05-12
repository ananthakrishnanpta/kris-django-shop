from django.shortcuts import render
from .models import CartItem

# Create your views here.
def viewCart(request):
    context = {
        'items' : CartItem.objects.filter(user = request.user)
    }
