# pysoccerdata
A simple python package for extracting real-time soccer data from diverse online sources, providing essential statistics and insights.

### Installation
```
pip install fuchibol
```

### Usage
Simple usage, please read the docs.
```py
import fuchibol

client = fuchibol.client()
matchs = client.get_matchs()

for match in matchs:
  print(match)
```
### Constributions
All constributions, bug reports or fixes and ideas are welcome.
