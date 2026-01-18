from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    """
    Represents a poll with a title, description, and an owner.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polls")

    def __str__(self) -> str:
        """
        Returns the string representation of the poll.
        """
        return self.title


class Option(models.Model):
    """
    Represents an option within a poll that users can vote for.
    """
    poll: models.ForeignKey = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="options",
    )
    text: models.CharField = models.CharField(max_length=255)
    votes: models.PositiveIntegerField = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        """
        Returns the string representation of the option.
        """
        return f"{self.text} ({self.votes})"
