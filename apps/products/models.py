from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Product(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    designation = models.CharField(max_length=100)
    qte_stock = models.DecimalField(max_digits=30, decimal_places=3)
    value = models.DecimalField(max_digits=30, decimal_places=3)

    def __str__(self):
        return self.designation

    class Meta:
        pass
        # ordering = ("-qte_stock", "-valeur_initial")


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
