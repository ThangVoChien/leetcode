from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr: List[int], set: set, i):
            if i >= len(nums):
                nums.append(arr)
                return

            for num in nums:
                if num not in set:
                    arr.append(num)
                    set.add(num)
                    
                    backtrack(arr, set, i+1)
                    
                    arr.pop()
                    set.remove(num)