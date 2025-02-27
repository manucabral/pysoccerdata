from typing import List
from .match_summary import MatchSummary
from .match_status import MatchStatus


def filter_by(matches: List[MatchSummary], status: MatchStatus) -> List[MatchSummary]:
    """
    Filter matches by status.

    Args:
        matches (List[MatchSummary]): A list of MatchSummary objects.
        status (MatchStatus): The status to filter.

    Returns:
        List[MatchSummary]: A list of MatchSummary objects.
    """
    return [match for match in matches if match.status == status]
