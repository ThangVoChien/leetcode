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
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                while backtrack(arr, sum, n+1):
                    n+=1
                    while n < len(candidates)-1 and candidates[n] == candidates[n+1]:
                        n+=1

                arr.pop()
                return True

        candidates.sort()

        i = 0
        while backtrack([], 0, i):
            i+=1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i+=1

        return sol