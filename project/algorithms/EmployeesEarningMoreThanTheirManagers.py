import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, left_on=['managerId'], right_on=['id'], suffixes=("", "_M"))
    employee = employee[employee["salary"] > employee["salary_M"]]
    return employee[['name']].rename(columns={'name': 'Employee'})