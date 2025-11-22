from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


# TODO Ampliar esse modelo para clientes
class CustomUser(User):
    address = ...
    orders = ...

# TODO Melhorar esse modelo para vendedores
class SellerUser(User):
    name = models.CharField(max_length=25)
    products = ...
    links = ...
    