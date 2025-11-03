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
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dict ={}

        dup = 0
        cur = 0
        ptr = 0

        while ptr < len(nums):
            num = nums[ptr]

            if num in dict:
                if dict[num] >= 2:
                    ptr+=1
                    continue
            else:
                dict[num] = 0

            nums[cur] = nums[ptr]
            dict[num] += 1

            cur+=1
            dup+=1
            ptr+=1

        return dup