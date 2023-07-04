"""
ASGI config for familygram project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path
from notifications.consumers import TestConsumer
from chat.consumers import ChatConsumer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "familygram.settings")

application = get_asgi_application()


websocket_urlpatterns = [
    re_path(r"ws/notifications/$", TestConsumer.as_asgi()),
    re_path(r"ws/chats/$", ChatConsumer.as_asgi()),
]


application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
