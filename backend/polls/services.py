from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from typing import Any
from .models import Poll, Option

def vote_for_option(poll: Poll, option_id: int) -> dict[str, Any]:
    """
    Registers a vote and notifies WebSocket clients.
    """
    from django.db import transaction

    with transaction.atomic():
        # Lock the option row
        option = Option.objects.select_for_update().get(id=option_id, poll=poll)
        option.votes += 1
        option.save()

    # Refresh options from database to get updated votes
    options = Option.objects.filter(poll=poll).values("id", "text", "votes")

    result = {
        "poll_id": poll.id,
        "options": list(options),
    }

    # Send to WebSocket group
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"poll_{poll.id}",
        {"type": "vote_update", "message": result},
    )

    return result
