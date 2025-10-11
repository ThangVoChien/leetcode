from typing import List
from dataStructures.BinaryHeap import maxHeap

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = maxHeap(stones)

        while len(heap.vals) > 1:
            s1 = heap.pop()
            s2 = heap.pop()

            s = abs(s1 - s2)
            heap.append(s)

        if len(heap.vals) == 0:
            return 0
        else:
            return heap.vals[0]