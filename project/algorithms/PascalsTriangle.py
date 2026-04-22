from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = []
        
        pascal = []
        for i in range(numRows):
            p = []
            s = 0
            for j in pascal:
                s += j
                p.append(s)
                s = j
            p.append(1)
            sol.append(p.copy())
            pascal = p

        return sol
    
    def getRow(self, rowIndex: int) -> List[int]:
        def dynamic(row):
            if row == 0:
                return [1]

            pascal = dynamic(row-1)

            p = []
            s = 0
            for j in pascal:
                s += j
                p.append(s)
                s = j
            p.append(1)

            return p
        return dynamic(rowIndex)