from algorithms.DuplicateEmails import *
from dataStructures import *

print(duplicate_emails(schema("""
| id | email           |
| -- | --------------- |
| 1  | jacky@yahoo.com |
| 2  | jacky@yahoo.com |
| 3  | jacky@yahoo.com |
""")))