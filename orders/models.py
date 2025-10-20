from django.db import models
from django.conf import settings
from django.utils import timezone
from products.models import Product


class Order(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = "pending"
        PAID = "paid"
        SHIPPED = "shipped"
        DELIVERED = "delivered"
        CANCELED = "canceled"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Customer",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoice.choices,
        default=StatusChoice.PENDING,
        verbose_name="Order Status",
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Total price"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Заказ №{self.id} от {self.user}"

    def calculate_total(self):
        total = sum(item.total_price for item in self.items.all())
        self.total_price = total
        self.save()
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items", verbose_name="orders"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена на момент покупки"
    )

    class Meta:
        verbose_name = "Product in order"
        verbose_name_plural = "Products in orders"

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"
