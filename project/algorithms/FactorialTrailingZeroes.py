import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        sol = 0
        while n > 0:
            n //= 5
            sol += n
        return sol