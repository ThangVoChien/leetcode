import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])
    
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=['product'], var_name='quarter', value_name='sales')
    
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = "month", columns = 'city', values = 'temperature')