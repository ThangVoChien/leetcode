from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []

        def backtrack(arr: List[int], sum, n):
            if n == len(candidates):
                return False
            
            arr.append(candidates[n])
            sum += candidates[n]

            if sum >= target:
                if sum == target:
                    sol.append(arr.copy())

                arr.pop()
                return False
            else:
                while backtrack(arr, sum, n):
                    n+=1
                
                arr.pop()
                return True

        candidates.sort()

        i = 0
        while backtrack([], 0, i):
            i+=1

        return sol