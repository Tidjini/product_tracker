from pathlib import Path
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage

# Create your models here.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
fs = FileSystemStorage(location=BASE_DIR / "media")


class Product(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    designation = models.CharField(max_length=100)
    qte_stock = models.DecimalField(max_digits=30, decimal_places=3)
    value = models.DecimalField(max_digits=30, decimal_places=3)
    qte_picture = models.FileField(blank=True, null=True, max_length=1024, storage=fs)
    value_picture = models.FileField(blank=True, null=True, max_length=1024, storage=fs)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.designation

    class Meta:
        ordering = ("-update_at", "-value", "-qte_stock")


class Movement(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="updates"
    )
    qte = models.DecimalField(max_digits=30, decimal_places=3)
    value = models.DecimalField(max_digits=30, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    in_out = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at", "-in_out", "qte")


@receiver(post_save, sender=Movement)
def update_product(instance, created, **kwargs):
    if created:
        instance.product.qte_stock += instance.qte
        instance.product.value += instance.value
        instance.product.save()
