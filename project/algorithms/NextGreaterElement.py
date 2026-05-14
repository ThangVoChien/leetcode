from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        map = {i: -1 for i in nums1}

        for i in range(len(nums2)-1):
            while i < len(nums2)-1 and nums2[i] > nums2[i+1]:
                n = nums2.pop(i+1)
                if n in map:
                    j = i+1
                    while j < len(nums2) and nums2[j] < n:
                        j+=1
                    if j < len(nums2):
                        map[n] = nums2[j]

        next = nums2.pop()
        while len(nums2) > 0:
            n = nums2.pop()
            if n in map:
                map[n] = next
            next = n

        for n in nums1:
            sol.append(map[n])

        return sol