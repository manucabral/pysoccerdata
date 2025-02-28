"""
Contains the MatchSummary class.
"""
from datetime import datetime
from dataclasses import dataclass, field
from .match_status import MatchStatus


@dataclass
class MatchSummary:
    """
    Represents a match summary.
    """

    _id: int = field(metadata={"doc": "Unique id"})
    status: MatchStatus = field(metadata={"doc": "Current status"})
    info: str = field(metadata={"doc": "Simple slug"})
    start_time: datetime = field(metadata={"doc": "Start time of the match"})
