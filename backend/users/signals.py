from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, BuyerProfile, SellerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'buyer':
            BuyerProfile.objects.create(user=instance)
        elif instance.user_type == 'seller':
            SellerProfile.objects.create(user=instance)
