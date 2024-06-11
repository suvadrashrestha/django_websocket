
from django.urls import path
from .consumers import MyAsyncJsonWebsocketConsumer
websocket_urlpatterns=[
 path('ws/async/<str:groupname>/',MyAsyncJsonWebsocketConsumer.as_asgi())
]