from django.db.models import *
from django.utils.text import slugify

def product_image_upload_path(instance, filename):
    product_name = slugify(instance.product.name)  # Convert product name to a slug
    return f'products/{product_name}/{filename}'

class Product(Model):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    desc = TextField(max_length=500)

    def __str__(self):
        return f"Product : {self.name}"

class ProductImage(Model):
    img = ImageField(upload_to=product_image_upload_path)
    default = BooleanField(default=False)
    product = ForeignKey(Product, on_delete=CASCADE, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"
