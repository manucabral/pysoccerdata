"""
The main client to interact with the library.
"""

from typing import List
from .utils import get_today
from .services import SofascoreClient
from .match import (
    MatchSummary,
    MatchDetails,
    MatchCard,
    MatchStats,
    parse_match_team,
    parse_match_stats,
    parse_match_cards,
    MatchStatus,
    IncidentType,
)


class Client:
    """
    The main core class.
    """

    def __init__(self):
        """
        Initialize the client.
        """
        self.__sofascore: SofascoreClient = SofascoreClient()

    def get_matchs(self, date: str = None) -> List[MatchSummary]:
        """
        Get all matchs from a specific date.

        Args:
            date (str): The date to get the matchs. Format: "YYYY-MM-DD". Defaults to today.

        Returns:
            List[MatchSummary]: A list of MatchSummary objects.

        Note:
            If you want all match details use the get_match_by_id method.
        """
        date = date or get_today()
        events = self.__sofascore.get_events(date)
        return [
            MatchSummary(
                _id=event.get("id"),
                status=MatchStatus(event.get("status", {}).get("type", "notstarted")),
                info=event.get("slug"),
            )
            for event in events
        ]

    def get_match_stats(self, match_id: int) -> MatchStats:
        """
        Get all stats from a specific match.

        Args:
            match_id (int): The match id.

        Returns:
            dict: A dictionary with all match stats.
        """
        stats = self.__sofascore.get_stats(match_id)
        return parse_match_stats(stats)

    def get_match_details(self, match_id: int) -> MatchDetails:
        """
        Get all details from a specific match.

        Args:
            match_id (int): The match id.

        Returns:
            dict: A dictionary with all match details.
        """
        _match = self.__sofascore.get_event(match_id)
        stats = self.get_match_stats(match_id)
        return MatchDetails(
            _id=_match.get("id"),
            home_team=parse_match_team(_match, "homeScore", "homeTeam"),
            away_team=parse_match_team(_match, "awayScore", "awayTeam"),
            stats=stats,
            cards=self.get_match_cards(match_id),
        )

    def get_match_incidents(self, match_id: int) -> dict:
        """
        Get all incidents from a specific match.

        Args:
            match_id (int): The match id.

        Returns:
            dict: A dictionary with all match incidents.
        """
        return self.__sofascore.get_incidents(match_id)

    def get_match_cards(self, match_id: int) -> List[MatchCard]:
        """
        Get all given cards from a specific match.

        Args:
            match_id (int): The match id.

        Returns:
            dict: A dictionary with all match cards.
        """
        incidents = self.get_match_incidents(match_id)
        card_incidents = [
            incident
            for incident in incidents
            if incident.get("incidentType") == IncidentType.CARD.value
        ]
        return parse_match_cards(card_incidents)

    def get_team_details(self, team_id: int) -> dict:
        """
        Get all details from a specific team.

        Args:
            team_id (int): The team id.

        Returns:
            dict: A dictionary with all team details.
        """
        return self.__sofascore.get_team(team_id)
