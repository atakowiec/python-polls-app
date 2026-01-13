from rest_framework.routers import DefaultRouter
from polls.views import PollViewSet, my_polls
from django.urls import path
from .views import register
from .views import create_poll, delete_poll

router = DefaultRouter()
router.register("", PollViewSet, basename="poll")

urlpatterns = [
    path("register/", register, name="register"),
    path("create/", create_poll, name="create_poll"),
    path("<int:poll_id>/delete/", delete_poll, name="delete_poll"),
    path("me/", my_polls, name="my_polls"),
    *router.urls
]
