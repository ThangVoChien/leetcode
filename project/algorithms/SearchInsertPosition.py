from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == len(nums)-1 or nums[mid+1] > target:
                    return mid+1
                else:
                    start+=1
            else:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    end-=1