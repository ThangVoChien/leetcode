from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def backtrack(arr: List[int], set: set):
            if len(arr) == len(nums):
                sol.append(arr.copy())
                return

            for num in nums:
                if num not in set:
                    arr.append(num)
                    set.add(num)

                    backtrack(arr, set)
                    
                    arr.pop()
                    set.remove(num)

        backtrack([], set())
        return sol