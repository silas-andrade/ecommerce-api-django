from django.db.models import *
from django.db import models

from apps.users.models import SellerUser


# TODO Pensar melhor se o seller vai ser uma herança direta do Usuário
# ELe pode ser uma loja que não terá relacionamento com o usuário
class Product(models.Model):
    seller = ForeignKey(SellerUser, editable=False, on_delete=CASCADE)
    name = CharField(max_length=255)
    price = DecimalField(decimal_places=2, max_digits=10)
    # pictures = ImageField()