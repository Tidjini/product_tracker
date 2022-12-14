from datetime import datetime
from pathlib import Path

# django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

# application
from apps.core.services import NotificationAPI
from apps.core.constants import *
from ..storage import OverwriteStorage


BASE_DIR = Path(__file__).parent.parent.parent.parent
fs = OverwriteStorage(location=BASE_DIR / "media")


class FactureCharge(models.Model):

    ENTITY = ("P", "PROMAG"), ("INF", "INFRABITUM")

    number = models.CharField(max_length=15, null=True)
    designation = models.CharField(max_length=100, null=True)
    entity = models.CharField(max_length=5, choices=ENTITY, default="INF")
    remarque = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    sender = models.CharField(max_length=15, null=True)
    update_at = models.DateField(auto_now=True)
    confirm = models.BooleanField()
    picture = models.FileField(blank=True, null=True, max_length=1024)
    montant = models.DecimalField(max_digits=30, decimal_places=3, default=0)


@receiver(post_save, sender=FactureCharge)
def after_save(sender, instance, created, **kwargs):
    push_notification(instance)


def push_notification(facture):
    now = datetime.now()
    data = {
        "date": now,
        "message": f"""{facture.number} a était mis à jours. date {now:%d-%m-%Y} at:{now:%H:%M}""",
        "sender": facture.sender,
        "context": "FACTURE",
    }
    NotificationAPI.push(NOTIFICATION_PUSH_END, data=data)
