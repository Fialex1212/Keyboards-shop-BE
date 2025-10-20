from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = (
        "user",
        "status",
        "total_price",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "status",)
