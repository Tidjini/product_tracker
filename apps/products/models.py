from datetime import datetime
from pathlib import Path
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save, post_save

from apps.core import constants
from apps.core.services import NotificationAPI
from .storage import OverwriteStorage
from . import helpers

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

    @property
    def tonne(self):
        T, kg = divmod(self.qte_stock, 1000)
        if kg:
            return "{} T and {:.2f} Kg".format(T, kg)
        return f"{T} T"

    def __str__(self):
        return self.designation

    class Meta:
        ordering = ("-update_at", "-value", "-qte_stock")


class ProductAPI:
    @staticmethod
    def get_item_by_id(reference):
        try:
            return Product.objects.get(reference=reference)
        except Product.DoesNotExist:
            return None


@receiver(post_save, sender=Product)
def post_notification(sender, instance, created, **kwargs):
    if created:
        push_notification(instance)


@receiver(pre_save, sender=Product)
def pre_notification(sender, instance, **kwargs):
    # if new do nothing
    if not instance.pk:
        return

    # get old version
    old = ProductAPI.get_item_by_id(instance.pk)
    if not old:
        return

    # if there is no difference, do nothing
    if old.qte_stock == instance.qte_stock and old.value == instance.value:
        return
    push_notification(instance)


def push_notification(product):
    now = datetime.now()
    message = helpers.creation_message(product, now)
    data = helpers.built_data(product, message, now)
    NotificationAPI.push(constants.NOTIFICATION_PUSH_END, data=data)
