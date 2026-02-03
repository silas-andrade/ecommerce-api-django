from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Um campo para diferenciar o tipo de usuário
    USER_TYPE_CHOICES = (
        ("customer", "Customer"),
        ("seller", "Seller"),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


# TODO Ampliar esse modelo para clientes

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    links = models.TextField(null=True, blank=True)
    