"""
ASGI config for django_channel_web_socket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel_web_socket.settings')
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routing
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
           app.routing.websocket_urlpatterns
        )
    )
})
