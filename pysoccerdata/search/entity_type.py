from enum import Enum

class EntityType(Enum):
    """
    Enum with all entity types.
    """
    
    ALL = "all"
    TEAM = "teams"
    PLAYER = "player-team-persons"
    TOURNAMENT = "unique-tournaments"
    MATCH = "events"