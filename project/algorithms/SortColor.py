from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quicksort(left, right):
            if left >= right:
                return

            pivot = nums[right]
            i = left - 1

            for j in range(left, right):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[right] = nums[right], nums[i+1]
            p = i + 1

            quicksort(left, p - 1)
            quicksort(p + 1, right)
        quicksort(0, len(nums)-1)
