from django.urls import re_path,path

from .consumers.chat_consumers import ChatConsumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name/',ChatConsumers)
    # re_path(r'ws/chat/<str:room_name>/',ChatConsumers),
    # re_path(r'^ws/chat/(?P<room_name>[^/]+)/', ChatConsumers),
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumers),
]