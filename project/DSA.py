from algorithms.RankScores import *
from dataStructures import *

print(order_scores(schema("""
| id | score |
| -- | ----- |
| 1  | 3.5   |
| 2  | 3.65  |
| 3  | 4     |
| 4  | 3.85  |
| 5  | 4     |
| 6  | 3.65  |
""")))