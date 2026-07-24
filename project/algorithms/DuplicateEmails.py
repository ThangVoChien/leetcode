import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = person[person.duplicated(subset=["email"])].drop_duplicates(subset=["email"])
    return person[["email"]].rename(columns={"email": "Email"})