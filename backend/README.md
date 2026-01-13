# Polls & Voting Backend

Backend application built with Django, Django REST Framework and Django Channels.

## Features
- REST API for polls and voting
- WebSocket real-time updates
- Server status WebSocket
- Unit tests with pytest

## Setup (Windows)

```powershell
docker compose up -d
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
