from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, -1, -1):
            n =  target - nums[i]
            if n in nums:
                id = nums.index(n)
                if id != i:
                    numList = list()
                    numList.append(id)
                    numList.append(i)
                    return numList
                
    def twoSum2(self, numbers, target):
        start = 0
        end = len(numbers) - 1

        while start < end:
            total = numbers[start] + numbers[end]

            if total == target:
                return [start + 1, end + 1]
            elif total < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]