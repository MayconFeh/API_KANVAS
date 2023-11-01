from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "name", "video_url", "content"]
        extra_kwargs = {
            "video_url": {"required": False}
        }
