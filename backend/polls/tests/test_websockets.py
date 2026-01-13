import pytest
from channels.testing import WebsocketCommunicator
from config.asgi import application
from polls.models import Poll, Option
import asyncio

@pytest.mark.asyncio
@pytest.mark.django_db
async def test_poll_websocket_connection():
    poll = Poll.objects.create(title="Async poll")
    communicator = WebsocketCommunicator(application, f"/ws/polls/{poll.id}/")
    connected, _ = await communicator.connect()
    assert connected
    await communicator.disconnect()

@pytest.mark.asyncio
async def test_server_status_websocket():
    communicator = WebsocketCommunicator(application, "/ws/status/")
    connected, _ = await communicator.connect()
    assert connected

    message = await communicator.receive_json_from()
    assert "status" in message
    assert "datetime" in message

    await communicator.disconnect()
