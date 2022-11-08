from django.db import models

# Create your models here.


class Product(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    designation = models.CharField(max_length=100)
    qte_stock = models.DecimalField(max_digits=30, decimal_places=3)
    valeur_initial = models.DecimalField(max_digits=30, decimal_places=3)
    valeur_actuel = models.DecimalField(max_digits=30, decimal_places=3)


class Movement(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="updates"
    )
    qte = models.DecimalField(max_digits=30, decimal_places=3)
    value = models.DecimalField(max_digits=30, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    in_out = models.BooleanField(default=True)
