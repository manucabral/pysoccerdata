"""
In this example, we will get the first match from the list of
finished matches (2025-01-01) and print all the cards of the match.

The output will be something like this:
Arsenal 3 vs Brentford 1

Player: R. Calafiori (957602)
Minute: 57
Reason: Foul
Value: yellow
Is Home: False

Player: C. Nørgaard (135256)
Minute: 26
Reason: Foul
Value: yellow
Is Home: True

Player: J. Timber (958959)
Minute: 17
Reason: Foul
Value: yellow
Is Home: False
"""

import pysoccerdata

client = pysoccerdata.Client()
matchs = client.get_matchs("2025-01-01")
matchs_finished = pysoccerdata.filter_by(matchs, pysoccerdata.MatchStatus.FINISHED)

target_match = matchs_finished[0]
details = client.get_match_details(target_match._id)

print(
    f"{details.away_team.name} {details.away_team.score} vs {details.home_team.name} {details.home_team.score}"
)

for card in details.cards:
    print(
        f"""
Player: {card.player.name} ({card.player._id})
Minute: {card.minute}
Reason: {card.reason}
Value: {card.value}
Is Home: {card.is_home}
    """
    )
