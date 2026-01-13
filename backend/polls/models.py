from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polls")

    def __str__(self):
        return self.title


class Option(models.Model):
    poll: models.ForeignKey = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="options",
    )
    text: models.CharField = models.CharField(max_length=255)
    votes: models.PositiveIntegerField = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.text} ({self.votes})"
