from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        j = 1
        r = nums2[0]

        for i in range(m+n):
            if nums1[i] > r or nums1[i] == 0:
                t = r
                r = nums1[i]
                nums1[i] = t

                while j < n and (nums2[j] < r or r == 0):
                    t = r
                    r = nums2[j]
                    nums2[j] = t
                    if nums2[j] == 0:
                        j+=1