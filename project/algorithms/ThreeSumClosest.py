from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sol = target

        nums.sort()
        for i in range(len(nums) - 2):
            x = nums[i]
            if x > target:
                break

            y = target - x
            start = i + 1
            end = len(nums) - 1

            while start < end:
                z = nums[start] + nums[end]

                if z == y:
                    sol = target
                    break

                if z < y:
                    start += 1
                else:
                    end -= 1

            if sol == target:
                break
            
        return sol