from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from polls.models import Poll
from typing import Any


class IsPollActive(BasePermission):
    """
    Custom permission to only allow voting on active polls.
    """
    def has_permission(self, request: Request, view: Any) -> bool:
        """
        Check if the poll is active based on the 'pk' in view kwargs.
        """
        poll_id: int | None = view.kwargs.get("pk")
        if poll_id is None:
            return True

        try:
            poll: Poll = Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            return False

        return poll.is_active
