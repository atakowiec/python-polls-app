import pytest
from polls.models import Poll, Option

@pytest.mark.django_db
def test_poll_creation(user):
    poll = Poll.objects.create(title="New Poll", description="Desc", owner=user)
    assert str(poll) == "New Poll"
    assert poll.is_active is True

@pytest.mark.django_db
def test_option_creation(poll):
    option = Option.objects.create(poll=poll, text="New Option")
    assert str(option) == "New Option (0)"
    assert option.votes == 0
