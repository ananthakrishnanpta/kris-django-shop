from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm
from .models import CustomUser

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class BuyerDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'buyer_dashboard.html'

    def test_func(self):
        return self.request.user.user_type == 'buyer'

class SellerDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'seller_dashboard.html'

    def test_func(self):
        return self.request.user.user_type == 'seller'

