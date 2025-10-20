from rest_framework import serializers
from discounts.models import Disount


class DisountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disount
        fields = [
            "code",
            "product",
            "activated_by",
            "created_at",
            "used_at",
        ]
