from django.db import models
from django.conf import settings


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="review",
        verbose_name="Customer",
        null=True,
        blank=True,
    )
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User review"
        verbose_name_plural = "Users reviews"

    def __str__(self):
        return f"{self.user} - {self.rating}"
