from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from .models import Product
from apps.core.services import NotificationAPI
from apps.core import constants

from datetime import datetime
from . import helpers


@receiver(post_save, sender=Product)
def send_notification(instance, created, **kwargs):
    now = datetime.now()

    # if created:
    message = helpers.creation_message(instance, now)
    data = helpers.built_data(instance, message, now)
    NotificationAPI.push(constants.NOTIFICATION_PUSH_END, data=data)
