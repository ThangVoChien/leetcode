from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, -1, -1):
            n =  target - nums[i]
            if n in nums:
                id = nums.index(n)
                if id != i:
                    numList = list()
                    numList.append(id)
                    numList.append(i)
                    return numList