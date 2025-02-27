"""
Contains the Match class.
"""

from dataclasses import dataclass, field
from .match_team import MatchTeam
from .match_stats import MatchStats


@dataclass
class MatchDetails:
    """
    Represents a match.
    """

    _id: int = field(metadata={"doc": "Unique id"})
    home_team: MatchTeam = field(metadata={"doc": "Home team"})
    away_team: MatchTeam = field(metadata={"doc": "Away team"})
    stats: MatchStats = field(metadata={"doc": "Match stats"})
