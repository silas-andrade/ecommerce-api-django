import uuid
from pathlib import Path

from django.db import models

from apps.users.models import Seller


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    seller = models.ForeignKey(
        Seller,
        related_name="products", 
        editable=False, 
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    
def product_image_path(instance, filename):
    ext = Path(filename).suffix  # ".jpg", ".png"
    new_filename = f"{uuid.uuid4()}{ext}"
    return f"products/images/{instance.product.id}/{new_filename}"


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
        )
    
    image = models.ImageField(upload_to=product_image_path)

    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
