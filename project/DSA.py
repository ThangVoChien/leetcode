from algorithms.FillMissingData import *
from dataStructures import *

print(fillMissingValues(schema("""
| name            | quantity | price |
| --------------- | -------- | ----- |
| Wristwatch      | null     | 135   |
| WirelessEarbuds | null     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
""")))