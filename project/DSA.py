from algorithms.CombineTwoTables import *
from dataStructures import *

print(combine_two_tables(schema("""
| personId | lastName | firstName |
| -------- | -------- | --------- |
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
"""), schema("""
| addressId | personId | city          | state      |
| --------- | -------- | ------------- | ---------- |
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
""")))