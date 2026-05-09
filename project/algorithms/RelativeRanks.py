from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = score
        heap.sort(reverse=True)

        map = {v: k for k, v in enumerate(heap)}

        sol = []
        for s in score:
            m = map[s]
            if m == 0:
                m = "Gold Medal"
            elif m == 1:
                m = "Silver Medal"
            elif m == 2:
                m = "Bronze Medal"
            else:
                m = str(m)
            sol.append(map[s])

        return map