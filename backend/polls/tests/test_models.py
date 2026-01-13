import pytest
from polls.models import Poll, Option


@pytest.mark.django_db
def test_poll_creation():
    poll = Poll.objects.create(title="Favorite color?", description="Choose one")
    assert poll.id is not None
    assert poll.is_active is True
    assert poll.title == "Favorite color?"


@pytest.mark.django_db
def test_option_creation():
    poll = Poll.objects.create(title="Favorite color?")
    option = Option.objects.create(poll=poll, text="Red")
    assert option.id is not None
    assert option.votes == 0
    assert option.poll == poll
