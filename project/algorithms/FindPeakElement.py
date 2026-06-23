from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (end + start) // 2
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums)-1 and nums[mid] > nums[mid-1]) or (nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                return mid
            else:
                if mid != len(nums)-1 and (mid == 0 or nums[mid] < nums[mid+1]):
                    start = mid + 1
                else:
                    end = mid - 1