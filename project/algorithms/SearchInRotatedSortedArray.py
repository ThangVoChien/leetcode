from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = nums[0]
        if target == k:
            return 0

        rotated = target < k

        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end + start) // 2
            r = nums[mid] < k

            if nums[mid] == target:
                return mid
            elif (rotated == r and target < nums[mid]) or (rotated != r and target > nums[mid]):
                print(rotated, r)
                end = mid - 1
            else:
                start = mid + 1

        return -1