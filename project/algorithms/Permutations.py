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
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sol = []
        map = {}

        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num] = 0

        def backtrack(arr: List[int], dict: dict):
            if len(arr) == len(nums):
                sol.append(arr.copy())
                return

            for num in map:
                if num not in dict or dict[num] < map[num]:
                    arr.append(num)
                    if num in dict:
                        dict[num]+=1
                    else:
                        dict[num] = 0

                    backtrack(arr, dict)
                    
                    arr.pop()
                    dict[num]-=1

        backtrack([], {})
        return sol