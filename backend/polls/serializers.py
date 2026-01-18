from rest_framework import serializers
from .models import Poll, Option

from typing import Any


class OptionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Option model.
    """
    class Meta:
        model = Option
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    """
    Serializer for the Poll model, including its options and owner.
    """
    options = OptionSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Poll
        fields = "__all__"


class PollCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new Poll with options.
    """
    options = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=True,
        min_length=2,
    )

    class Meta:
        model = Poll
        fields = ["title", "description", "is_active", "options"]

    def create(self, validated_data: dict[str, Any]) -> Poll:
        """
        Creates a new Poll and its associated options.
        """
        options_data = validated_data.pop("options")
        poll = Poll.objects.create(**validated_data, owner=self.context["request"].user)
        # create options
        for opt_text in options_data:
            Option.objects.create(poll=poll, text=opt_text)
        return poll
