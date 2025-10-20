from rest_framework import serializers
from products.models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "alt_text"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    final_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "discounted_price",
            "final_price",
            "type",
            "quantity",
            "created_at",
            "updated_at",
            "images",
        ]