from django.db import models
from django.db.models import *

import uuid

from apps.users.models import Customer 

# TODO Adicionar modelos relacionados a pedidos, como Pedido, Item do Pedido, e Status do Pedido, e relaciona-los com o modelo de Usuário.

class Order(models.Model):

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('PA', 'Paid'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('C', 'Canceled'),
    ]
    
    user = ForeignKey(Customer, on_delete=DO_NOTHING, editable=False)
    order_id = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = CharField(max_length=2, choices=STATUS_CHOICES, default='P')
    total_amount = DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.order_id)}"



class OrderItem(models.Model):
    ...
