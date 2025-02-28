"""
The main client to interact with the library.
"""

from datetime import datetime
from typing import List, Union
from .utils import get_today
from .services import SofascoreClient
from .match import (
    MatchSummary,
    MatchDetails,
    MatchCard,
    MatchStats,
    MatchGoal,
    parse_match_team,
    parse_match_stats,
    parse_match_cards,
    parse_match_goals,
    MatchStatus,
    IncidentType,
)
from .search import EntityType, parse_entity_search
from .tournament import TournamentCategory


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
                start_time=datetime.fromtimestamp(event.get("startTimestamp")),
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
        win_probability = self.get_win_probability(match_id)
        return MatchDetails(
            _id=_match.get("id"),
            home_team=parse_match_team(
                _match, "homeScore", "homeTeam", win_probability
            ),
            away_team=parse_match_team(
                _match, "awayScore", "awayTeam", win_probability
            ),
            stats=stats,
            cards=self.get_match_cards(match_id),
            goals=self.get_match_goals(match_id),
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

    def get_match_goals(self, match_id: int) -> List[MatchGoal]:
        """
        Get all goals from a specific match.

        Args:
            match_id (int): The match id.

        Returns:
            dict: A dictionary with all match goals.
        """
        incidents = self.get_match_incidents(match_id)
        goals = [
            incident
            for incident in incidents
            if incident.get("incidentType") == IncidentType.GOAL.value
        ]
        return parse_match_goals(goals)

    def get_win_probability(self, match_id: int) -> dict:
        """
        Get the win probability from a specific match.

        Args:
            match_id (int): The match id.

        Returns:
            dict: A dictionary with the win probability.
        """
        return self.__sofascore.get_win_probability(match_id)

    def get_team_details(self, team_id: int) -> dict:
        """
        Get all details from a specific team.

        Args:
            team_id (int): The team id.

        Returns:
            dict: A dictionary with all team details.
        """
        return self.__sofascore.get_team(team_id)

    def get_tournaments_by_category(
        self, category_id: Union[int, TournamentCategory]
    ) -> dict:
        """
        Get all tournaments from a specific category.

        Args:
            category_id (TournamentCategory): The category id.

        Returns:
            dict: A dictionary with all tournaments from a specific category.
        """
        _id = None
        if not isinstance(category_id, TournamentCategory):
            _id = category_id
        else:
            _id = category_id.value
        return self.__sofascore.get_tournaments_by_category(_id)

    def search(
        self, query: str, entity: Union[str, EntityType] = "all"
    ) -> Union[List[MatchSummary], List[dict]]:
        if isinstance(entity, EntityType):
            entity = entity.value
        raw_results = self.__sofascore.search(query, entity)
        if entity == EntityType.MATCH.value:
            return [
                MatchSummary(
                    _id=result["entity"].get("id"),
                    status=MatchStatus(
                        result["entity"].get("status", {}).get("type", "notstarted")
                    ),
                    info=result["entity"].get("slug"),
                    start_time=datetime.fromtimestamp(
                        result["entity"].get("startTimestamp")
                    ),
                )
                for result in raw_results
            ]

        # for all results we use the parse_entity_search method
        return parse_entity_search(raw_results)
