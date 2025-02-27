from dataclasses import dataclass, field


@dataclass
class MatchPlayer:
    _id: int = field(default=0, metadata={"doc": "Unique id"})
    name: str = field(default="No name", metadata={"doc": "Player name"})
    full_name: str = field(default="No full name", metadata={"doc": "Player full name"})
    slug: str = field(default="No slug", metadata={"doc": "Player slug"})
    jersey_number: int = field(default=0, metadata={"doc": "Player jersey number"})