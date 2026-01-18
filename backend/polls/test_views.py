import pytest
from django.urls import reverse
from unittest.mock import patch, AsyncMock
from polls.models import Poll, Option

@pytest.mark.django_db
class TestPollViewSet:
    def test_list_polls(self, api_client, poll):
        url = reverse("poll-list")
        response = api_client.get(url)
        assert response.status_code == 200
        titles = [p["title"] for p in response.data]
        assert poll.title in titles

    def test_retrieve_poll(self, api_client, poll):
        url = reverse("poll-detail", kwargs={"pk": poll.id})
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data["title"] == poll.title
        assert len(response.data["options"]) == 2

    def test_vote_on_poll(self, api_client, poll):
        option = poll.options.first()
        url = reverse("poll-vote", kwargs={"pk": poll.id})
        
        with patch("polls.services.get_channel_layer") as mock_get_channel_layer:
            mock_channel_layer = mock_get_channel_layer.return_value
            mock_channel_layer.group_send = AsyncMock()
            
            response = api_client.post(url, {"option_id": option.id}, format="json")
            assert response.status_code == 200
            assert response.data["poll_id"] == poll.id
            
            option.refresh_from_db()
            assert option.votes == 1

@pytest.mark.django_db
class TestAuthViews:
    def test_register(self, api_client):
        url = reverse("register")
        data = {"username": "newuser", "password": "StrongPassword123!"}
        response = api_client.post(url, data)
        assert response.status_code == 201
        assert response.data["message"] == "User created"

    def test_create_poll(self, auth_client):
        url = reverse("create_poll")
        data = {
            "title": "Created Poll",
            "description": "Created Description",
            "options": ["Opt A", "Opt B"]
        }
        response = auth_client.post(url, data, format="json")
        assert response.status_code == 201
        assert Poll.objects.filter(title="Created Poll").exists()
        assert Option.objects.filter(text="Opt A").exists()

    def test_delete_poll(self, auth_client, poll):
        url = reverse("delete_poll", kwargs={"poll_id": poll.id})
        response = auth_client.delete(url)
        assert response.status_code == 204
        assert not Poll.objects.filter(id=poll.id).exists()

    def test_delete_someone_elses_poll(self, auth_client, user):
        from django.contrib.auth.models import User
        other_user = User.objects.create_user(username="other", password="password")
        other_poll = Poll.objects.create(title="Other", description="Other", owner=other_user)
        
        url = reverse("delete_poll", kwargs={"poll_id": other_poll.id})
        response = auth_client.delete(url)
        assert response.status_code == 404

    def test_my_polls(self, auth_client, poll):
        url = reverse("my_polls")
        response = auth_client.get(url)
        assert response.status_code == 200
        titles = [p["title"] for p in response.data]
        assert poll.title in titles
