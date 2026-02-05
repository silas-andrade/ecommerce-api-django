from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_profile'
    )
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Customer: {self.user.username}"
    

class Seller(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='seller_profile'
    )
    #photo = models.ImageField()
    store_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Seller: {self.store_name}"


"""
if hasattr(user, 'seller_profile'):
    # é seller

if hasattr(user, 'customer_profile'):
    # é customer
"""