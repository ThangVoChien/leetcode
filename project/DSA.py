from algorithms.DropDuplicateRows import *
from dataStructures import *

print(dropDuplicateEmails(schema("""
| customer_id | name    | email               |
| ----------- | ------- | ------------------- |
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
""")))