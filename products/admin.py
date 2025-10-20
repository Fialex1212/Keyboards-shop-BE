from django.contrib import admin
from products.models import Product, ProductImage, ProductAttribute


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductImageInline]
    list_display = ("title", "image", "price", "discounted_price", "quantity")
