from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = float("-inf")

        for i in range(len(nums)):
            num = nums[i]
            if num > max:
                max = num
            for j in range(i+1, len(nums)):
                num *= nums[j]
                if num > max:
                    max = num

        return max