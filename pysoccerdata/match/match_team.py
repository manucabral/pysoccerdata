"""
Contains the MatchTeam class.
"""

import typing
from dataclasses import dataclass, field


@dataclass
class MatchTeam:
    """
    Represents a match summary.
    """

    _id: int = field(metadata={"doc": "Unique id"})
    name: str = field(metadata={"doc": "Team name"})
    score: int = field(metadata={"doc": "Team score"})


def parse_match_team(data: typing.Dict, score_key: str, team_key: str) -> MatchTeam:
    return MatchTeam(
        _id=data.get(team_key).get("id"),
        name=data.get(team_key).get("shortName"),
        score=data.get(score_key).get("current"),
    )
