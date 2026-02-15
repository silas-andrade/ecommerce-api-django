from django.db import models

import uuid

from .choices import OrderStatus
from core import settings
from core.models import UUIDModel, TimeStampedModel
from apps.products.models import Product



class Order(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="orders",
        on_delete=models.PROTECT
    )

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    shipping_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(UUIDModel, TimeStampedModel):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
        )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=1)