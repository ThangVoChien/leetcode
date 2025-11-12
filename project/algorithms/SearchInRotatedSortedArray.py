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
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def search2(self, nums: List[int], target: int) -> bool:
        k = nums[0]
        if target == k:
            return True
        if target < k and target > nums[len(nums)-1]:
            return False

        rotated = target < k

        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (end + start) // 2

            i = mid
            if mid != 0 and nums[mid] == k:
                i-=1
                while i > 0 and nums[i] == k:
                    i-=1

                if nums[i] == target:
                    return True

            r = nums[i] < k

            if nums[mid] == target:
                return True
            elif (rotated == r and target < nums[mid]) or (rotated != r and target > nums[mid]):
                end = mid - 1
            else:
                start = mid + 1

        return False