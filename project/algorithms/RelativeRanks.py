from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sol = []

        heap = score.copy()
        heap.sort(reverse=True)

        map = {v: k for k, v in enumerate(heap)}
        for s in score:
            m = map[s]
            if m == 0:
                m = "Gold Medal"
            elif m == 1:
                m = "Silver Medal"
            elif m == 2:
                m = "Bronze Medal"
            else:
                m = str(m+1)
            sol.append(m)

        return sol