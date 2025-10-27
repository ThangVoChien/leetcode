from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        
        left = 0
        right = len(height)-1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > max:
                max = area

            if height[left] < height[right]:
                h = height[left]
                while height[left] <= h and left < right:
                    left+=1
            else:
                h = height[right]
                while height[right] <= h and left < right:
                    right-=1

        return max