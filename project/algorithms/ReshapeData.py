import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])
    
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    pass
    
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pass