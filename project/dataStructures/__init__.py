from .LinkedList import linkedList
from .BinaryTree import binaryTree
from .Graph import graph
import pandas as pd
import re

null = None

def schema(table: str) -> pd.DataFrame:
    data = []
    t = False
    column = null

    for row in table.strip().split('\n'):
        if column != null:
            if t:
                data.append(re.findall(r'(?<=\|)\s*([^|]+?)\s*(?=\|)', row))
            else:
                t = True
        else:
            column = re.findall(r'(?<=\|)\s*([^|]+?)\s*(?=\|)', row)

    frame =  pd.DataFrame(data, columns=column)
    if not frame.empty:
        frame = frame.astype(
            {
                column[i]: 
                'Int64' if re.match(r'^-?\d+$', data[0][i])
                else 'Float64' if re.match(r'^-?\d+\.\d+$', data[0][i])
                else 'datetime64[ns]' if re.match(r'^\d{4}-\d{2}-\d{2}$', data[0][i])
                else 'object'
                for i in range(len(column))
            }
        )

    return frame