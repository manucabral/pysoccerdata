"""
Contains the Match class.
"""

from dataclasses import dataclass, field



@dataclass
class MatchDetails:
    """
    Represents a match.
    """

    _id: int = field(metadata={"doc": "Unique id"})
    full_name: str = field(metadata={"doc": "Full name"})
    short_name: str = field(metadata={"doc": "Short name"})
    code: str = field(metadata={"doc": "Code"})