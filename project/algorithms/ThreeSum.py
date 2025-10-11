from typing import List

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []

        nums.sort()
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            x = nums[i]
            if x > 0:
                break

            y = 0 - x
            start = i + 1
            end = len(nums) - 1

            while start < end:                
                if start != i + 1 and nums[start] == nums[start-1]:
                    start += 1
                    continue

                if end != len(nums) - 1 and nums[end] == nums[end+1]:
                    end -= 1
                    continue

                z = nums[start] + nums[end]
                if z == y:
                    sol.append([x, nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif z < y:
                    start += 1
                else:
                    end -= 1
            
        return sol