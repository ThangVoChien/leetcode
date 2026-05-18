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
    
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        sol = [-1 for _ in nums]
        stack = []

        i = len(nums)-1
        max = float("-inf")
        j = -1
        while True:
            n = nums[i]
            if max == n and j == i:
                return sol
            while stack and stack[-1][0] <= n:
                stack.pop()
            if max < n:
                max = n
                j = i

            sol[i] = -1 if not stack else stack[-1][0]
            stack.append((n, i))

            if i == 0:
                i = len(nums)-1
            else:
                i-=1

    def nextGreaterElement3(self, n):
        digits = list(str(n))
        length = len(digits)
        pivot = -1

        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                digits[i], digits[pivot] = digits[pivot], digits[i]
                break

        digits[pivot + 1:] = digits[pivot + 1:][::-1]
        result = int(''.join(digits))

        return result if result <= 2**31 - 1 else -1
    
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1] * n
        stack = []
        second = []
        for i in range(n):
            while second and nums[i] > nums[second[-1]]:
                curr = second.pop()
                if output[curr] == -1:
                    output[curr] = nums[i]
            temp = []
            while stack and nums[i] > nums[stack[-1]]:
                curr = stack.pop()
                if output[curr] == -1:
                    temp.append(curr)
            stack.append(i)
            second += temp[::-1]
        return output