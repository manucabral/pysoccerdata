"""
Contains the MatchGoal class.
"""

from typing import List
from dataclasses import dataclass, field
from .match_player import MatchPlayer


@dataclass
class MatchGoal:
    """
    Represents a match goal incident.
    """

    _id: int = field(default=0, metadata={"doc": "Unique id"})
    player: MatchPlayer = field(default=MatchPlayer, metadata={"doc": "Player"})
    is_home: bool = field(
        default=False, metadata={"doc": "True if the player is from the home team"}
    )
    minute: int = field(default=0, metadata={"doc": "Minute when the goal was scored"})
    value: str = field(default="", metadata={"doc": "Goal value"})

def parse_match_goals(data: List[dict]) -> List[MatchGoal]:
    """
    Parse a list of match goals.

    Args:
        data (List[dict]): List of match goals.
    
    Returns:   
        List[MatchGoal]: List of parsed match goals.
    """
    return [
        MatchGoal(
            _id=item.get("id"),
            player=MatchPlayer(
                _id=item.get("player", {}).get("id"),
                name=item.get("player", {}).get("shortName"),
                full_name=item.get("player", {}).get("name"),
                slug=item.get("player", {}).get("slug"),
                jersey_number=item.get("player", {}).get("jerseyNumber"),
            ),
            is_home=item.get("isHome"),
            value=item.get("incidentClass"),
            minute=item.get("time"),
        )
        for item in data
    ]
