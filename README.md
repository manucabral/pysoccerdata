# pysoccerdata
A simple python package for extracting real-time soccer data from diverse online sources, providing essential statistics and insights.

### Installation
```
pip install pysoccerdata
```

### Usage
Simple example
```py
import pysoccerdata

client = pysoccerdata.client()
matchs = client.get_matchs()

for match in matchs:
  print(match)
```
Search matchs
```py
matchs = client.search("Real Madrid", pysoccerdata.EntityType.MATCH)
for match in matchs:
  print(match)
```
And more! Check out [examples](https://github.com/manucabral/pysoccerdata/tree/main/examples)

### Constributions
All constributions, bug reports or fixes and ideas are welcome.
