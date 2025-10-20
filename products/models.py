from django.db import models


class Product(models.Model):
    class TypeChoice(models.TextChoices):
        KEYBOARD = "keyboard"
        MOUSE = "mouse"
        HEADSET = "headset"
        MONITOR = "monitor"
        OTHER = "other"

    title = models.CharField(max_length=255, verbose_name="Product title")
    image = models.ImageField(upload_to="products/images/", null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Price", default=0
    )
    type = models.CharField(
        max_length=50,
        choices=TypeChoice.choices,
        default=TypeChoice.OTHER,
        verbose_name="Product type",
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Discounted price",
        default=0,
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"

    def __str__(self):
        return self.title

    @property
    def final_price(self):
        return self.discounted_price or self.price


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Product"
    )
    image = models.ImageField(upload_to="products/images/")
    alt_text = models.CharField(
        max_length=255, blank=True, verbose_name="Image description"
    )

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self):
        return f"Image for {self.product.title}"


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="attributes",
        verbose_name="Product",
    )
    title = models.CharField(max_length=255, verbose_name="Product attribute title")
    text = models.TextField(blank=True, null=True, verbose_name="Text")
