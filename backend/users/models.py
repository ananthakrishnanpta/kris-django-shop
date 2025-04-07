from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class BuyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)

class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=20)
