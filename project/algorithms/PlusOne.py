from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = 1
        i = len(digits)-1
        while r:
            if i < 0:
                digits = [1] + digits
                break

            digits[i]+=1
            if digits[i] != 10:
                r = 0
            else:
                digits[i] = 0
                i-=1
        return digits