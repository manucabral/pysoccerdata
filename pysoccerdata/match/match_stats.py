from dataclasses import dataclass, field
from ..utils import camel_to_snake
from .match_stats_item import (
    StatMatchItem,
    Overview,
    Shots,
    Attack,
    Passes,
    Duels,
    Defending,
    Goalkeeping,
)


@dataclass
class MatchStats:
    overview: Overview = field(default_factory=Overview)
    shots: Shots = field(default_factory=Shots)
    attack: Attack = field(default_factory=Attack)
    passes: Passes = field(default_factory=Passes)
    duels: Duels = field(default_factory=Duels)
    defending: Defending = field(default_factory=Defending)
    goalkeeping: Goalkeeping = field(default_factory=Goalkeeping)


def parse_match_stats(stats: list) -> MatchStats:
    groups_mapping = {
        "Match overview": Overview,
        "Shots": Shots,
        "Attack": Attack,
        "Passes": Passes,
        "Duels": Duels,
        "Defending": Defending,
        "Goalkeeping": Goalkeeping,
    }
    results = {}
    for group in stats:
        group_name = group.get("groupName")
        if group_name in groups_mapping:
            cls = groups_mapping[group_name]
            group_data = {}
            for item in group.get("statisticsItems", []):
                key = camel_to_snake(item.get("key", ""))
                group_data[key] = StatMatchItem(
                    name=item.get("name"),
                    home=item.get("homeValue"),
                    away=item.get("awayValue"),
                    result=item.get("statisticsType"),
                )
            results[group_name] = cls(**group_data)
    return MatchStats(
        overview=results.get("Match overview"),
        shots=results.get("Shots"),
        attack=results.get("Attack"),
        passes=results.get("Passes"),
        duels=results.get("Duels"),
        defending=results.get("Defending"),
        goalkeeping=results.get("Goalkeeping"),
    )
