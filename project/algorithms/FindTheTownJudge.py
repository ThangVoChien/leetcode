from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p1 = {i: 0 for i in range(1, n+1)}
        p2 = {i: 0 for i in range(1, n+1)}

        for t in trust:
            p1[t[0]]+=1
            p2[t[1]]+=1

        for i in range(1, n+1):
            if p1[i] == 0 and p2[i] == n-1:
                return i
                
        return -1