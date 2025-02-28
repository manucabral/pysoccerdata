"""
This is a simple example of how to get all in progress matches in real-time.

The output will be something like this:

Identifier:  13292240 rosario-central-boca-juniors
Boca Juniors 1 vs 0 Rosario Central
Status:  1st half
Period elapsed:  12 minutes
Total elapsed:  13 minutes

Identifier:  13333168 sportivo-ameliano-recoleta-fc
Recoleta 1 vs 1 Sportivo Ameliano
Status:  2nd half
Period elapsed:  50 minutes
Total elapsed:  118 minutes

Note: If you want all match details use the get_match_details method.
"""

import pysoccerdata

client = pysoccerdata.Client()

result = client.get_matchs()
in_progress_matches = pysoccerdata.filter_by(
    result, pysoccerdata.MatchStatusType.IN_PROGRESS
)

for match in in_progress_matches:

    print("Identifier: ", match._id, match.info)
    print(match.home_team, match.home_score, "vs", match.away_score, match.away_team)
    print("Status: ", match.status.description)
    print("Period elapsed: ", match.time.current_period_minutes, "minutes")
    print("Total elapsed: ", match.time.elapsed_minutes, "minutes")

    print("")
