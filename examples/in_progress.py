"""
This is a simple example of how to get all in progress matches in real-time.

The output will be something like this:

12420335 - fk-radnicki-1923-fk-novi-pazar
12420333 - fk-tsc-backa-topola-fk-cukaricki
13012879 - zed-fc-zamalek-sc
13267727 - al-arabi-sc-al-rayyan
13330198 - ajman-al-nasr-dubai
13330200 - al-wahda-fc-al-ain
13243180 - ludogorets-botev-plovdiv
13152103 - viktoria-plzen-fc-zlin
12442063 - hvidovre-fc-fredericia
12568456 - vfb-oldenburg-sv-werder-bremen-ii-u23
13485867 - sc-chabab-mohammedia-moghreb-atletico-tetuan
13203891 - puszcza-niepolomice-polonia-warszawa
12618872 - steaua-bucuresti-csm-ceahlaul-piatra-neamt
13542286 - sc-rothis-rw-rankweil

Note: If you want all match details use the get_match_details method.
"""

import pysoccerdata

client = pysoccerdata.Client()
matchs = client.get_matchs()

in_progress_matchs = pysoccerdata.filter_by(
    matchs, pysoccerdata.MatchStatus.IN_PROGRESS
)

for match in in_progress_matchs:
    print(f"{match._id} - {match.info}")
