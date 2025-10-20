from django.db import models
from orders.models import Order
from django.conf import settings


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_payment",
        verbose_name="Customer",
        null=True,
        blank=True,
    )
    provider = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, default="pending")
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.user} - {self.provider} ({self.status})"
