from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        def gray(n: int):
            return n ^ (n >> 1)
        
        g = []
        for i in range(2**n):
            x = gray(i)
            g.append(x)

        return g