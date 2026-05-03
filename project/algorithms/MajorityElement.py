from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
    def majorityElement2(self, nums: List[int]) -> List[int]:
        sol = []
        map = {}

        max = len(nums) / 3
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

            if map[n] > max:
                sol.append(n)
                map[n] = -max

        return sol