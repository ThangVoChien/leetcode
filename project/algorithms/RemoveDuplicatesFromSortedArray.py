from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dup = 0
        cur = 0
        ptr = 0

        while ptr < len(nums):
            if ptr != 0 and nums[ptr] == nums[ptr-1]:
                ptr+=1
                continue

            nums[cur] = nums[ptr]
            cur+=1
            dup+=1
            ptr+=1

        return dup