from pathlib import Path
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

from apps.core import constants
from apps.core.services import NotificationAPI
from .storage import OverwriteStorage

# Create your models here.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
fs = OverwriteStorage(location=BASE_DIR / "media")


class Product(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    designation = models.CharField(max_length=100)
    qte_stock = models.DecimalField(max_digits=30, decimal_places=3)
    value = models.DecimalField(max_digits=30, decimal_places=3)
    picture = models.FileField(blank=True, null=True, max_length=1024, storage=fs)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.designation

    class Meta:
        ordering = ("-update_at", "-value", "-qte_stock")


@receiver(post_save, sender=Product)
def notify(instance, created, **kwargs):
    data = {"this": "is", "me": "from"}
    NotificationAPI.push(url=constants.NOTIFICATION_API, data=data)
