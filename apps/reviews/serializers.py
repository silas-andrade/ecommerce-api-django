from rest_framework import serializers

from .models import (
    Review,
    ReviewMedia,
    ReviewReaction
)
from .constants import MAX_REVIEW_IMAGE_SIZE, MAX_REVIEW_VIDEO_SIZE
from apps.users.serializers import ReadUserSerializer



class CreateReviewMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewMedia
        fields = ['file', 'media_type', 'order']
    
    def validate(self, attrs):
        file = attrs["file"]
        content_type = file.content_type

        if content_type.startswith("image/") and file.size > MAX_REVIEW_IMAGE_SIZE:
            raise serializers.ValidationError("Very large image (max 5MB).")

        if content_type.startswith("video/") and file.size > MAX_REVIEW_VIDEO_SIZE:
            raise serializers.ValidationError("Very large video (max 30MB).")

        return attrs


class ReadReviewMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewMedia
        fields = [
            'id',
            'review',
            'file',
            'media_type',
            'order',
        ]


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']

    #TODO Validar se o produto está publicado ou não para publicação

class ReadReviewSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer(read_only=True)
    media = ReadReviewMediaSerializer(read_only=True, many=True)
    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'product', 
            'text',
            'media',
            'created_at'
            ]


class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']



class CreateReviewReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReaction
        fields = ['id', 'review', 'is_helpful']