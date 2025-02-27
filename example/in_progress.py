import pysoccerdata

client = pysoccerdata.Client()
matchs = client.get_matchs()
in_progress = pysoccerdata.filter_by(matchs, pysoccerdata.MatchStatus.IN_PROGRESS)
for match in in_progress:
    print(match)