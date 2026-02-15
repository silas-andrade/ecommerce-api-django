from django.db import models

import uuid

from .storage import review_media_path
from core import settings
from core.models import UUIDModel, TimeStampedModel
from apps.products.models import Product


class Review(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name="reviews",
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product,
        related_name="reviews",
        on_delete=models.CASCADE
        )
    text = models.TextField()


class ReviewMedia(UUIDModel, TimeStampedModel):
    review = models.ForeignKey(
        Review, 
        related_name="media", 
        on_delete=models.CASCADE
        )
    
    file = models.FileField(
        upload_to=review_media_path
        )

    media_type = models.CharField(
        max_length=10,
        choices=[
            ("image", "Image"),
            ("video", "Video"),
            ]
        )
    
    order = models.PositiveIntegerField(default=0)

class ReviewReaction(UUIDModel, TimeStampedModel):
    review = models.ForeignKey(
        Review,
        related_name="reactions",
        on_delete=models.CASCADE
        )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="review_reactions",
        on_delete=models.CASCADE
        )
    
    is_helpful = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["review", "user"],
                name="unique_review_reaction"
            )
        ]