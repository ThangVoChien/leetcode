from algorithms.NthHighestSalary import *
from dataStructures import *

print(nth_highest_salary(schema("""
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
"""), 1))