from typing import TypedDict, List


class OptionVotes(TypedDict):
    id: int
    votes: int


class PollResults(TypedDict):
    poll_id: int
    options: List[OptionVotes]
