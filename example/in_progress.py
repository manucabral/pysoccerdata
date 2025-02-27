import fuchibol

client = fuchibol.Client()
matchs = client.get_matchs()
in_progress = fuchibol.filter_by(matchs, fuchibol.MatchStatus.IN_PROGRESS)
for match in in_progress:
    print(match)