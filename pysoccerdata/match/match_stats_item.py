from dataclasses import dataclass, field


def default_stat_match_item():
    return StatMatchItem(name="No data", home=0.0, away=0.0, result="No data")


@dataclass
class StatMatchItem:
    name: str = ""
    home: float = 0.0
    away: float = 0.0
    result: str = ""


@dataclass
class Overview:
    ball_possession: StatMatchItem = field(default_factory=default_stat_match_item)
    expected_goals: StatMatchItem = field(default_factory=default_stat_match_item)
    big_chance_created: StatMatchItem = field(default_factory=default_stat_match_item)
    total_shots_on_goal: StatMatchItem = field(default_factory=default_stat_match_item)
    goalkeeper_saves: StatMatchItem = field(default_factory=default_stat_match_item)
    corner_kicks: StatMatchItem = field(default_factory=default_stat_match_item)
    fouls: StatMatchItem = field(default_factory=default_stat_match_item)
    passes: StatMatchItem = field(default_factory=default_stat_match_item)
    total_tackle: StatMatchItem = field(default_factory=default_stat_match_item)
    free_kicks: StatMatchItem = field(default_factory=default_stat_match_item)
    yellow_cards: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class Shots:
    total_shots_on_goal: StatMatchItem = field(default_factory=default_stat_match_item)
    shots_on_goal: StatMatchItem = field(default_factory=default_stat_match_item)
    hit_woodwork: StatMatchItem = field(default_factory=default_stat_match_item)
    shots_off_goal: StatMatchItem = field(default_factory=default_stat_match_item)
    blocked_scoring_attempt: StatMatchItem = field(default_factory=default_stat_match_item)
    total_shots_inside_box: StatMatchItem = field(default_factory=default_stat_match_item)
    total_shots_outside_box: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class Attack:
    big_chance_scored: StatMatchItem = field(default_factory=default_stat_match_item)
    big_chance_missed: StatMatchItem = field(default_factory=default_stat_match_item)
    accurate_through_ball: StatMatchItem = field(default_factory=default_stat_match_item)
    touches_in_opp_box: StatMatchItem = field(default_factory=default_stat_match_item)
    fouled_final_third: StatMatchItem = field(default_factory=default_stat_match_item)
    offsides: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class Passes:
    accurate_passes: StatMatchItem = field(default_factory=default_stat_match_item)
    throw_ins: StatMatchItem = field(default_factory=default_stat_match_item)
    final_third_entries: StatMatchItem = field(default_factory=default_stat_match_item)
    final_third_phase_statistic: StatMatchItem = field(default_factory=default_stat_match_item)
    accurate_long_balls: StatMatchItem = field(default_factory=default_stat_match_item)
    accurate_cross: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class Duels:
    duel_won_percent: StatMatchItem = field(default_factory=default_stat_match_item)
    dispossessed: StatMatchItem = field(default_factory=default_stat_match_item)
    ground_duels_percentage: StatMatchItem = field(default_factory=default_stat_match_item)
    aerial_duels_percentage: StatMatchItem = field(default_factory=default_stat_match_item)
    dribbles_percentage: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class Defending:
    won_tackle_percent: StatMatchItem = field(default_factory=default_stat_match_item)
    total_tackle: StatMatchItem = field(default_factory=default_stat_match_item)
    interception_won: StatMatchItem = field(default_factory=default_stat_match_item)
    ball_recovery: StatMatchItem = field(default_factory=default_stat_match_item)
    total_clearance: StatMatchItem = field(default_factory=default_stat_match_item)
    errors_lead_to_shot: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class Goalkeeping:
    goalkeeper_saves: StatMatchItem = field(default_factory=default_stat_match_item)
    goals_prevented: StatMatchItem = field(default_factory=default_stat_match_item)
    dive_saves: StatMatchItem = field(default_factory=default_stat_match_item)
    high_claims: StatMatchItem = field(default_factory=default_stat_match_item)
    punches: StatMatchItem = field(default_factory=default_stat_match_item)
    goal_kicks: StatMatchItem = field(default_factory=default_stat_match_item)


@dataclass
class MatchStats:
    overview: Overview = field(default_factory=Overview)
    shots: Shots = field(default_factory=Shots)
    attack: Attack = field(default_factory=Attack)
    passes: Passes = field(default_factory=Passes)
    duels: Duels = field(default_factory=Duels)
    defending: Defending = field(default_factory=Defending)
    goalkeeping: Goalkeeping = field(default_factory=Goalkeeping)
