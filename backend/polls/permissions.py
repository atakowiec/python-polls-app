from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from polls.models import Poll
from typing import Any


class IsPollActive(BasePermission):
    def has_permission(self, request: Request, view: Any) -> bool:
        poll_id: int | None = view.kwargs.get("pk")
        if poll_id is None:
            return True

        try:
            poll: Poll = Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            return False

        return poll.is_active
