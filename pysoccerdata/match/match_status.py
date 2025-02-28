from enum import Enum


class MatchStatus(Enum):
    FINISHED = "finished"
    NOT_STARTED = "notstarted"
    IN_PROGRESS = "inprogress"
    POSTPONED = "postponed"
    CANCELED = "canceled"
