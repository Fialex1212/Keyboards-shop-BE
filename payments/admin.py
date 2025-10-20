from django.contrib import admin
from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "order",
        "provider",
        "status",
        "transaction_id",
        "created_at",
    )
