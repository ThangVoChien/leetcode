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
    
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sol = 0

        nums1.sort()
        nums2.sort()
        nums3.sort()
        nums4.sort()
        for i in range(len(nums1)):
            if i != 0 and nums1[i] == nums1[i-1]:
                continue

            for j in range(len(nums2)):
                if j != 0 and nums2[j] == nums2[j-1]:
                    continue

                x = nums1[i] + nums2[j]

                y = 0 - x
                start = 0
                end = len(nums4) - 1

                while start < len(nums3) and end >= 0:
                    if start != 0 and nums3[start] == nums3[start-1]:
                        start += 1
                        continue

                    if end != len(nums4) - 1 and nums4[end] == nums4[end+1]:
                        end -= 1
                        continue

                    z = nums3[start] + nums4[end]
                    if z == y:
                        sol+=1
                        start += 1
                        end -= 1
                    elif z < y:
                        start += 1
                    else:
                        end -= 1
            
        return sol