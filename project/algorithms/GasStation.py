from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
                
        c = 0
        start = 0
        for i in range(len(gas)):
            c += gas[i] - cost[i]
            if c < 0:
                c = 0
                start = i + 1

        return start