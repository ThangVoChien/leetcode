from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divideConquer(arr: List[int]):
            if len(arr) == 1:
                return arr[0]

            mid = len(arr) // 2
            left = mid-1
            right = mid+1

            sol = arr[mid]

            maxLeft = float("-inf")
            sumLeft = 0
            while left >= 0:
                sumLeft += arr[left]
                maxLeft = max(maxLeft, sumLeft)
                left-=1

            maxRight = float("-inf")
            sumRight = 0
            while right < len(arr):
                sumRight += arr[right]
                maxRight = max(maxRight, sumRight)
                right+=1

            sol += (maxLeft if maxLeft >= 0 else 0) + (maxRight if maxRight >= 0 else 0)
            sol = max(sol, divideConquer(arr[:mid]), divideConquer(arr[mid:]))
            return sol

        sol = divideConquer(nums)
        return sol