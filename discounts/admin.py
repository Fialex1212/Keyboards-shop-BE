from django.contrib import admin
from discounts.models import Disount


@admin.register(Disount)
class DisountAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "product",
        "activated_by",
        "created_at",
    )
