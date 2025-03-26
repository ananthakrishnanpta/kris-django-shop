from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *

class HomeView(TemplateView):
    template_name = 'home.html'

class ProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImage.objects.all()
        return context