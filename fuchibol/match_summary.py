"""
Contains the MatchSummary class.
"""
from dataclasses import dataclass, field

@dataclass
class MatchSummary:
    """
    Represents a match summary.
    """
    _id: int = field(metadata={"doc": "Unique id"})
    status: str = field(metadata={"doc": "Current status"})
    info: str = field(metadata={"doc": "Simple slug"})