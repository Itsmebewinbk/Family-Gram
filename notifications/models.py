from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
import json



class Notification(models.Model):
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)
    # user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.notification


@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        notification_count = Notification.objects.filter(is_seen=False).count()
        data = {
            "count": notification_count,
            "current_notification": instance.notification,
        }
        async_to_sync(channel_layer.group_send)(
            "notification_group",
            {"type": "send_notification", "value": json.dumps(data)},
        )
