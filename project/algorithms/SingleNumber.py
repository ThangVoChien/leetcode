from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = 0
        for n in nums:
            sol ^= n
        return sol
    
    def singleNumber2(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for n in nums:
            one ^= n & ~two
            two ^= n & ~one
        return one
    
    def singleNumber3(self, nums: list[int]) -> list[int]:
        one = 0
        two = 0

        x = 0
        for n in nums:
            x ^= n

        b = 0
        while (x >> b) & 1 != 1:
            b += 1

        for n in nums:
            if (n >> b) & 1 == 1:
                one ^= n
            else:
                two ^= n

        return [one, two]