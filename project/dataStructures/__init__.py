from .LinkedList import linkedList
from .BinaryTree import binaryTree
from .Graph import graph
import pandas as pd
import re

null = None

def schema(table: str, type = None) -> pd.DataFrame:
    data = []
    ins = False
    column = null

    for row in table.strip().split('\n'):
        if column != null:
            if ins:
                n = re.findall(r'(?<=\|)\s*([^|]+?)\s*(?=\|)', row)
                for i in range(len(n)):
                    if n[i] == 'null':
                        n[i] = None
                data.append(n)
            else:
                ins = True
        else:
            column = re.findall(r'(?<=\|)\s*([^|]+?)\s*(?=\|)', row)

    frame = pd.DataFrame(data, columns=column)
    if not frame.empty:
        if type == None:
            frame = frame.astype(
                {
                    c: 
                    'Int64' if re.match(r'^-?\d+$', frame[c].dropna().iloc[0])
                    else 'Float64' if re.match(r'^-?\d+\.\d+$', frame[c].dropna().iloc[0])
                    else 'datetime64[ns]' if re.match(r'^\d{4}-\d{2}-\d{2}$', frame[c].dropna().iloc[0])
                    else 'object'
                    for c in column
                }
            )
        else:
            frame = frame.astype(type)

    return frame