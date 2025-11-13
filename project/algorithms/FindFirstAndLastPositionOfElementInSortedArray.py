from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = -1
        e = -1

        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                s = mid
                while s > start and nums[s-1] == target:
                    s-=1

                e = mid
                while e < end and nums[e+1] == target:
                    e+=1

                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [s, e]