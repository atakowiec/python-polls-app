from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from polls.models import Poll
from polls.serializers import PollSerializer
from polls.permissions import IsPollActive
from polls.services import vote_for_option
from typing import Any
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PollCreateSerializer


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.prefetch_related("options").all()
    serializer_class = PollSerializer

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsPollActive],
        url_path="vote",
    )
    def vote(self, request: Request, pk: int | None = None) -> Response:
        poll: Poll = self.get_object()
        option_id: int | None = request.data.get("option_id")

        if option_id is None:
            return Response(
                {"detail": "option_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result: dict[str, Any] = vote_for_option(poll, option_id)
        return Response(result, status=status.HTTP_200_OK)


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_poll(request):
    serializer = PollCreateSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        poll = serializer.save()
        return Response({"id": poll.id, "message": "Poll created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_poll(request, poll_id: int):
    try:
        poll = Poll.objects.get(id=poll_id, owner=request.user)
    except Poll.DoesNotExist:
        return Response({"error": "Poll not found or not owned"}, status=status.HTTP_404_NOT_FOUND)
    poll.delete()
    return Response({"message": "Poll deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_polls(request):
    polls = request.user.polls.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)
