from enum import Enum


class IncidentType(Enum):
    PERIOD = "period"
    CARD = "card"
    INJURY_TIME = "injuryTime"
    SUBSTITUTION = "substitution"
    GOAL = "goal"
