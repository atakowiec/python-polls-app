import pytest
from unittest.mock import patch, AsyncMock
from polls.services import vote_for_option

@pytest.mark.django_db
def test_vote_for_option(poll):
    option = poll.options.first()
    
    with patch("polls.services.get_channel_layer") as mock_get_channel_layer:
        mock_channel_layer = mock_get_channel_layer.return_value
        mock_channel_layer.group_send = AsyncMock()
        
        result = vote_for_option(poll, option.id)
        
        option.refresh_from_db()
        assert option.votes == 1
        assert result["poll_id"] == poll.id
        assert len(result["options"]) == poll.options.count()
        
        mock_channel_layer.group_send.assert_called_once()
        args, kwargs = mock_channel_layer.group_send.call_args
        assert args[0] == f"poll_{poll.id}"
        assert args[1]["type"] == "vote_update"
