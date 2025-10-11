from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []

        nums.sort()
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j-1]:
                    continue

                x = nums[i] + nums[j]

                y = target - x
                start = j + 1
                end = len(nums) - 1

                while start < end:
                    if start != j + 1 and nums[start] == nums[start-1]:
                        start += 1
                        continue

                    if end != len(nums) - 1 and nums[end] == nums[end+1]:
                        end -= 1
                        continue

                    z = nums[start] + nums[end]
                    if z == y:
                        sol.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                    elif z < y:
                        start += 1
                    else:
                        end -= 1
            
        return sol