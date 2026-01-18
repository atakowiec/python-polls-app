import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from polls.models import Poll, Option

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="password123")

@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def poll(user):
    p = Poll.objects.create(title="Test Poll", description="Test Description", owner=user)
    Option.objects.create(poll=p, text="Option 1")
    Option.objects.create(poll=p, text="Option 2")
    return p
