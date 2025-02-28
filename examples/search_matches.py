"""
In this example we will search for Real Madrid matches using the search method from the Client class.
The EntityType enum is used to specify the type of entity to search for.
In this case, we are searching for matches, so we use EntityType.MATCH.

Output:
13511923 atletico-madrid-real-madrid MatchStatus.NOT_STARTED 2025-03-04 17:00:00
13511924 atletico-madrid-real-madrid MatchStatus.NOT_STARTED 2025-03-12 17:00:00
12437865 real-madrid-real-betis MatchStatus.NOT_STARTED 2025-03-01 14:30:00
...
"""

from pysoccerdata import Client, EntityType, MatchSummary

client = Client()

# The result is a list of MatchSummary objects because we are searching for matches
result: list[MatchSummary] = client.search("Real Madrid", EntityType.MATCH)

for match in result:
    print(match._id, match.info, match.status, match.start_time)
    # for more details you can use the get_match_details method