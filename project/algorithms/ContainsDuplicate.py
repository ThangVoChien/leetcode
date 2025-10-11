from typing import List

class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i, num in enumerate(nums):
            if seen.get(num) != None and i - seen[num] <= k:
                return True
            seen[num] = i
        return False