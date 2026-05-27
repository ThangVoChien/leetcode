from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        
        c = {}
        for i in range(len(gas)):
            j = gas[i] - cost[i]
            if j not in c:
                c[j] = [i]
            else:
                c[j].append(i)

        for i in sorted(list(c.keys()), reverse=True):
            for start in c[i]:
                j = start+1
                g = gas[start] - cost[start]
                while True:
                    if j == len(gas):
                        j = 0
                    if j == start:
                        return start

                    g += gas[j] - cost[j]
                    if g < 0:
                        break
                    j+=1
        return -1