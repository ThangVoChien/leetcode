from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end + start) // 2
            if mid != 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[0]