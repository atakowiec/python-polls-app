from django.urls import path
from polls.consumers import PollConsumer, ServerStatusConsumer

websocket_urlpatterns = [
    path("ws/polls/<int:poll_id>/", PollConsumer.as_asgi()),
    path("ws/status/", ServerStatusConsumer.as_asgi()),
]
