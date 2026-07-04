from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)

            s = abs(s1 - s2)
            heapq.heappush(heap, -s)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]