"""
Simple example to get the win probability of a in progress match.

This script will get all in progress matches and get the details of the first one.
Then it will print the win probability of both teams.

Example output:

West Ham 0 - 0 Leicester
Win probability: 51% - 20%

Note:
    If match status is not in progress, the win probability will be 0%.
"""
import pysoccerdata

client = pysoccerdata.Client()
matchs = client.get_matchs()
in_progress = pysoccerdata.filter_by(matchs, pysoccerdata.MatchStatus.IN_PROGRESS)

target_match = in_progress[0]
details = client.get_match_details(target_match._id)

print(
    f"""
{details.home_team.name} {details.home_team.score} - {details.away_team.score} {details.away_team.name}
Win probability: {details.home_team.win_probability}% - {details.away_team.win_probability}%
"""
)
