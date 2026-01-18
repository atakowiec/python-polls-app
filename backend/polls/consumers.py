from channels.generic.websocket import AsyncJsonWebsocketConsumer
from common.utils import get_server_status
from typing import Any
import asyncio


class PollConsumer(AsyncJsonWebsocketConsumer):
    """
    WebSocket consumer for real-time poll updates.
    """
    async def connect(self) -> None:
        """
        Invoked when a WebSocket connection is established.
        """
        self.poll_id: int = int(self.scope["url_route"]["kwargs"]["poll_id"])
        self.group_name: str = f"poll_{self.poll_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        """
        Invoked when the WebSocket connection is closed.
        """
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content: dict[str, Any], **kwargs: Any) -> None:
        """
        Invoked when JSON data is received from the client.
        """
        pass  # Clients don’t send anything; votes happen via REST

    async def vote_update(self, event: dict[str, Any]) -> None:
        """
        Sends a vote update message to the client.
        """
        await self.send_json(event)


class ServerStatusConsumer(AsyncJsonWebsocketConsumer):
    """
    WebSocket consumer that sends periodic server status updates.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the ServerStatusConsumer.
        """
        super().__init__(*args, **kwargs)
        self.running: bool | None = None

    async def connect(self) -> None:
        """
        Invoked when a WebSocket connection is established.
        Starts the status update loop.
        """
        await self.accept()
        self.running = True
        asyncio.create_task(self.send_status_loop())

    async def disconnect(self, close_code: int) -> None:
        """
        Invoked when the WebSocket connection is closed.
        Stops the status update loop.
        """
        self.running = False

    async def send_status_loop(self) -> None:
        """
        Periodic loop that sends server status to the client.
        """
        while self.running:
            status: dict[str, Any] = get_server_status()
            await self.send_json(status)
            await asyncio.sleep(.2)  # every .2 seconds
