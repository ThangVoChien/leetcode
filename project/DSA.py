from algorithms.SelectData import *
from dataStructures import *

print(selectData(schema("""
| student_id | name    | age |
| ---------- | ------- | --- |
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
""")))