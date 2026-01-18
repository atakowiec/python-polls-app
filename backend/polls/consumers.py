from channels.generic.websocket import AsyncJsonWebsocketConsumer
from common.utils import get_server_status
from typing import Any
import asyncio


class PollConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self) -> None:
        self.poll_id: int = int(self.scope["url_route"]["kwargs"]["poll_id"])
        self.group_name: str = f"poll_{self.poll_id}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content: dict[str, Any], **kwargs: Any) -> None:
        pass  # Clients don’t send anything; votes happen via REST

    async def vote_update(self, event: dict[str, Any]) -> None:
        await self.send_json(event)


class ServerStatusConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = None

    async def connect(self) -> None:
        await self.accept()
        self.running: bool = True
        asyncio.create_task(self.send_status_loop())

    async def disconnect(self, close_code: int) -> None:
        self.running = False

    async def send_status_loop(self) -> None:
        while self.running:
            status: dict[str, Any] = get_server_status()
            await self.send_json(status)
            await asyncio.sleep(.2)  # every .2 seconds
