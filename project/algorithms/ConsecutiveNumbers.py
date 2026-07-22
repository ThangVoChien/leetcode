import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.merge(logs, left_on='id', right_on=logs['id'] + 1, suffixes=('_l1', '_l2')).merge(logs, left_on='id_l1', right_on=logs['id'] - 1)
    return logs.loc[(logs['num_l1'] == logs['num_l2']) & (logs['num_l1'] == logs['num']), ['num_l1']].drop_duplicates().rename(columns={'num_l1': 'ConsecutiveNums'})