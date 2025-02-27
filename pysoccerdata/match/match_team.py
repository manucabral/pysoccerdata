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
    win_probability: int = field(default=0, metadata={"doc": "Win probability"})


def parse_match_team(
    data: typing.Dict, score_key: str, team_key: str, win_prob: dict
) -> MatchTeam:
    details = MatchTeam(
        _id=data.get(team_key).get("id"),
        name=data.get(team_key).get("shortName"),
        score=data.get(score_key).get("current"),
    )
    if win_prob:
        details.win_probability = win_prob.get(
            "homeWin" if team_key == "homeTeam" else "awayWin"
        )
    return details
