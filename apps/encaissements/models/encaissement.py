from datetime import datetime
from pathlib import Path

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver


from apps.core import constants
from apps.core.services import NotificationAPI

from ..storage import OverwriteStorage


BASE_DIR = Path(__file__).parent.parent.parent.parent
fs = OverwriteStorage(location=BASE_DIR / "media")


class Encaissement(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    label = models.CharField(max_length=100)
    date_range = models.CharField(max_length=50, null=True)
    value = models.DecimalField(max_digits=30, decimal_places=3)
    previous_value = models.DecimalField(max_digits=30, decimal_places=3)
    update_at = models.DateTimeField(auto_now=True)
    picture = models.FileField(blank=True, null=True, max_length=1024)

    @property
    def growth_loss(self):
        if not self.previous_value:
            return 100

        if not self.value and not self.previous_value:
            return 0

        diff = self.value - self.previous_value
        percent = 100
        try:
            percent, _ = divmod(diff * 100, self.previous_value + diff)
        except:
            percent = 100
        return percent


class EncaissementAPI:
    @staticmethod
    def get_item_by_id(reference):
        try:
            return Encaissement.objects.get(reference=reference)
        except Encaissement.DoesNotExist:
            return None


@receiver(pre_save, sender=Encaissement)
def pre_notification(sender, instance, **kwargs):
    # if new do nothing
    if not instance.pk:
        return

    # get old version
    old = EncaissementAPI.get_item_by_id(instance.pk)
    if not old:
        return

    # if there is no difference, do nothing
    if old.value == instance.value:
        return
    push_notification(instance)


@receiver(post_save, sender=Encaissement)
def post_notification(sender, instance, created, **kwargs):

    # if new encaissement, send notification
    if created:
        push_notification(instance)


def push_notification(encaissement):
    now = datetime.now()
    data = {
        "date": now,
        "message": f"""{encaissement.reference} a ??tait mis ?? jours. date {now:%d-%m-%Y} at:{now:%H:%M}""",
        "context": "ENCAISSEMENT",
    }
    NotificationAPI.push(constants.NOTIFICATION_PUSH_END, data=data)
