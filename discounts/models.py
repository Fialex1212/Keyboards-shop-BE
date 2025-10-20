from django.db import models
from orders.models import Order


class Disount(models.Model):
    code = models.CharField(max_length=12, unique=True)
    product = models.ForeignKey(Order, on_delete=models.CASCADE)
    activated_by = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True, blank=True)

    def is_used(self):
        return self.activated_by is not None

    is_used.boolean = True
