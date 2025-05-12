from django.db import models
from shop.models import ProductListing
from users.models import BuyerProfile

# Create your models here.
class CartItem(models.Model):
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(ProductListing, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item.product.name} in {self.buyer.user.username}'s Cart - {self.quantity}."
    
