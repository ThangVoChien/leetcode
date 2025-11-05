from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        k = 0
        cur = 0
        ptr = 0

        while ptr < len(nums):
            if nums[ptr] == val:
                ptr+=1
                continue

            nums[cur] = nums[ptr]
            cur+=1
            k+=1
            ptr+=1

        return k