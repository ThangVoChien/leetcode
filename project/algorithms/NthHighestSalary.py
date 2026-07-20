import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    n = None

    if N > 0:
        salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
        if len(salary) >= N:
            n = salary.iloc[N-1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [n]})