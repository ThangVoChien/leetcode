from typing import List
from dataStructures.BinaryHeap import minHeap

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = minHeap()

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.nums.vals) == self.k and val < self.nums.vals[0]:
            return self.nums.vals[0]

        self.nums.append(val)

        if len(self.nums.vals) > self.k:
            self.nums.pop()

        return self.nums.vals[0]