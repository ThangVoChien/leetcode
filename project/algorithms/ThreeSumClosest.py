from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sol = -9999 if target >= 0 else 9999

        nums.sort()
        for i in range(len(nums) - 2):
            x = nums[i]

            y = target - x
            start = i + 1
            end = len(nums) - 1

            while start < end:
                z = nums[start] + nums[end]

                if z == y:
                    sol = target
                    break

                if abs(sol - target) > abs(x + z - target):
                    sol = x + z

                if z < y:
                    start += 1
                else:
                    end -= 1

            if sol == target:
                break
            
        return sol