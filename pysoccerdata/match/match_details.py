"""
Contains the Match class.
"""
from typing import List
from dataclasses import dataclass, field
from .match_team import MatchTeam
from .match_stats import MatchStats
from .match_cards import MatchCard
from .match_goal import MatchGoal


@dataclass
class MatchDetails:
    """
    Represents a match.
    """

    _id: int = field(metadata={"doc": "Unique id"})
    home_team: MatchTeam = field(metadata={"doc": "Home team"})
    away_team: MatchTeam = field(metadata={"doc": "Away team"})
    stats: MatchStats = field(metadata={"doc": "Match stats"})
    cards: List[MatchCard] = field(metadata={"doc": "Match cards"})
    goals: List[MatchGoal] = field(metadata={"doc": "Match goals"})
