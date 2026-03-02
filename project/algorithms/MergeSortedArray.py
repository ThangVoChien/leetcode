from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        j = 0
        r = []
        l = m

        for i in range(m+n):
            while j < n:
                if nums2[j] < nums1[i]:
                    r.append(nums2[j])
                    j+=1
                else:
                    break

            if len(r) != 0 or i >= l:
                if nums1[i] != 0 or (nums1[i] == 0 and i < l):
                    r.append(nums1[i])
                else:
                    l+=1

                if len(r) != 0:
                    nums1[i] = r.pop(0)
                elif j < n:
                    nums1[i] = nums2[j]
                    j+=1