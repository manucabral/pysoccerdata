"""
This module contains the IncidentType enum.
"""
from enum import Enum


class IncidentType(Enum):
    """
    Enum class for incident types.
    """
    PERIOD = "period" # TODO: Implement
    CARD = "card"
    INJURY_TIME = "injuryTime" # TODO: Implement
    SUBSTITUTION = "substitution" # TODO: Implement
    GOAL = "goal"
