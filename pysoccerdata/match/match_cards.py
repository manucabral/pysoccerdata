"""
Contains the MatchCards class.
"""

from typing import List
from dataclasses import dataclass, field
from .match_player import MatchPlayer


@dataclass
class MatchCard:
    """
    Represents a match card incident.
    """

    _id: int = field(default=0, metadata={"doc": "Unique id"})
    player: MatchPlayer = field(default=MatchPlayer, metadata={"doc": "Player"})
    is_home: bool = field(
        default=False, metadata={"doc": "True if the player is from the home team"}
    )
    rescinded: bool = field(
        default=False, metadata={"doc": "True if the card was rescinded"}
    )
    value: str = field(default="", metadata={"doc": "Card value, can be yellow or red"})
    reason: str = field(default="", metadata={"doc": "Reason of the card"})
    minute: int = field(default=0, metadata={"doc": "Minute when the card was given"})
    added_time: int = field(default=0, metadata={"doc": "Time added by the referee"})


def parse_match_cards(data: List[dict]) -> List[MatchCard]:
    """
    Parse a list of match cards.

    Args:
        data (List[dict]): List of match cards.

    Returns:
        List[MatchCard]: List of parsed match cards.
    """
    return [
        MatchCard(
            _id=item.get("id"),
            player=MatchPlayer(
                _id=item.get("player", {}).get("id"),
                name=item.get("player", {}).get("shortName"),
                full_name=item.get("player", {}).get("name"),
                slug=item.get("player", {}).get("slug"),
                jersey_number=item.get("player", {}).get("jerseyNumber"),
            ),
            is_home=item.get("isHome"),
            rescinded=item.get("rescinded"),
            value=item.get("incidentClass"),
            reason=item.get("reason"),
            minute=item.get("time"),
            added_time=item.get("addedTime") or 0,
        )
        for item in data
    ]
