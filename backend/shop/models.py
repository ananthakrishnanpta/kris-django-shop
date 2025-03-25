from django.db.models import *

# Create your models here.

class Product(Model):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    desc = TextField(max_length=500)

    def __str__(self):
        return f"Product : {self.name}"

class ProductImage(Model):
    img = ImageField(upload_to='products/')
    default = BooleanField(default=False)
    product = ForeignKey(Product, on_delete=CASCADE, null=True)
