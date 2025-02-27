import re
from dataclasses import dataclass


@dataclass
class StatMatchItem:
    name: str
    home: float
    away: float
    result: str


@dataclass
class Overview:
    ball_possession: StatMatchItem
    expected_goals: StatMatchItem
    big_chance_created: StatMatchItem
    total_shots_on_goal: StatMatchItem
    goalkeeper_saves: StatMatchItem
    corner_kicks: StatMatchItem
    fouls: StatMatchItem
    passes: StatMatchItem
    total_tackle: StatMatchItem
    free_kicks: StatMatchItem
    yellow_cards: StatMatchItem


@dataclass
class Shots:
    total_shots_on_goal: StatMatchItem
    shots_on_goal: StatMatchItem
    hit_woodwork: StatMatchItem
    shots_off_goal: StatMatchItem
    blocked_scoring_attempt: StatMatchItem
    total_shots_inside_box: StatMatchItem
    total_shots_outside_box: StatMatchItem


@dataclass
class Attack:
    big_chance_scored: StatMatchItem
    big_chance_missed: StatMatchItem
    accurate_through_ball: StatMatchItem
    touches_in_opp_box: StatMatchItem
    fouled_final_third: StatMatchItem
    offsides: StatMatchItem


@dataclass
class Passes:
    accurate_passes: StatMatchItem
    throw_ins: StatMatchItem
    final_third_entries: StatMatchItem
    final_third_phase_statistic: StatMatchItem
    accurate_long_balls: StatMatchItem
    accurate_cross: StatMatchItem


@dataclass
class Duels:
    duel_won_percent: StatMatchItem
    dispossessed: StatMatchItem
    ground_duels_percentage: StatMatchItem
    aerial_duels_percentage: StatMatchItem
    dribbles_percentage: StatMatchItem


@dataclass
class Defending:
    won_tackle_percent: StatMatchItem
    total_tackle: StatMatchItem
    interception_won: StatMatchItem
    ball_recovery: StatMatchItem
    total_clearance: StatMatchItem
    errors_lead_to_shot: StatMatchItem


@dataclass
class Goalkeeping:
    goalkeeper_saves: StatMatchItem
    goals_prevented: StatMatchItem
    dive_saves: StatMatchItem
    high_claims: StatMatchItem
    punches: StatMatchItem
    goal_kicks: StatMatchItem


@dataclass
class MatchStats:
    overview: Overview
    shots: Shots
    attack: Attack
    passes: Passes
    duels: Duels
    defending: Defending
    goalkeeping: Goalkeeping
