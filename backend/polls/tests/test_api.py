import pytest
from rest_framework.test import APIClient
from polls.models import Poll, Option

@pytest.mark.django_db
def test_create_poll():
    client = APIClient()
    payload = {
        "title": "Best programming language?",
        "description": "Vote your favorite",
        "is_active": True,
        "options": [{"text": "Python"}, {"text": "JavaScript"}]
    }
    response = client.post("/api/polls/", payload, format="json")
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Best programming language?"
    assert len(data["options"]) == 2

@pytest.mark.django_db
def test_vote_endpoint():
    poll = Poll.objects.create(title="Language poll")
    option = Option.objects.create(poll=poll, text="Python")
    client = APIC
