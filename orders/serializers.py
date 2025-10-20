from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "order",
            "product",
            "quantity",
            "price",
            "total_price",
        ]


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "user",
            "status",
            "total_price",
            "created_at",
            "updated_at",
            "order_items",
        ]
