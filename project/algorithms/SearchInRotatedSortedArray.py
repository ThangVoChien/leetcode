from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = nums[0]
        if target == k:
            return 0

        rotated = True

        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start - end) // 2
            print(nums[mid])

            if nums[mid] >= k:
                rotated = True
            else:
                rotated = False

            if nums[mid] == k:
                return mid
            elif (nums[mid] > target and not rotated) or (nums[mid] < target and rotated):
                end = mid - 1
            else:
                start = mid + 1

        return -1