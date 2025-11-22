from django.db.models import *
from django.db import models

from accounts.models import SellerUser

class Product(models.Model):
    seller = ForeignKey(SellerUser, editable=False, on_delete=CASCADE)
    name = CharField(max_length=255)
    price = DecimalField(decimal_places=2, max_digits=10)
    # pictures = ImageField()