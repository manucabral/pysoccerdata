from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Country:
    alpha2: str
    alpha3: str
    name: str
    slug: str

@dataclass
class Sport:
    name: str
    slug: str
    id: int

@dataclass
class Category:
    id: int
    country: Country
    name: str
    slug: str
    sport: Sport
    flag: str
    alpha2: str

@dataclass
class UniqueTournament:
    name: str
    slug: str
    category: Category
    userCount: int
    id: int
    hasEventPlayerStatistics: bool
    displayInverseHomeAwayTeams: bool

@dataclass
class Tournament:
    name: str
    slug: str
    category: Category
    uniqueTournament: Optional[UniqueTournament] = None
    priority: int = 0
    id: int = 0

@dataclass
class Season:
    name: str
    year: str
    editor: bool
    id: int

@dataclass
class RoundInfo:
    round: int

@dataclass
class Status:
    code: int
    description: str
    type: str

# Para los equipos, incluimos colores y traducciones

@dataclass
class TeamColors:
    primary: str
    secondary: str
    text: str

@dataclass
class FieldTranslations:
    nameTranslation: Dict[str, str]
    shortNameTranslation: Dict[str, str]

@dataclass
class Team:
    name: str
    slug: str
    shortName: str
    gender: str
    sport: Sport
    userCount: int
    nameCode: str
    disabled: bool
    national: bool
    type: int
    id: int
    country: Country
    entityType: str
    subTeams: List  # Puede ser List[Team] u otro tipo, según el contexto
    teamColors: TeamColors
    fieldTranslations: FieldTranslations

# Clases para puntajes

@dataclass
class Score:
    current: int
    display: int
    period1: int
    period2: int
    normaltime: int

# Clases para tiempos

@dataclass
class TimeData:
    injuryTime1: int
    initial: int
    max: int
    extra: int
    currentPeriodStartTimestamp: int

@dataclass
class Changes:
    changes: List[str]
    changeTimestamp: int

@dataclass
class StatusTime:
    prefix: str
    initial: int
    max: int
    timestamp: int
    extra: int

# Clase principal que agrupa toda la información del evento

@dataclass
class Event:
    tournament: Tournament
    season: Season
    roundInfo: RoundInfo
    customId: str
    status: Status
    homeTeam: Team
    awayTeam: Team
    homeScore: Score
    awayScore: Score
    time: TimeData
    changes: Changes
    hasGlobalHighlights: bool
    hasEventPlayerStatistics: bool
    hasEventPlayerHeatMap: bool
    detailId: int
    crowdsourcingDataDisplayEnabled: bool
    id: int
    statusTime: StatusTime
    startTimestamp: int
    slug: str
    lastPeriod: str
    finalResultOnly: bool
    feedLocked: bool
    isEditor: bool
