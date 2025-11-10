from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        min = len(nums)-1
        while True:
            if nums[min] > nums[i]:
                min = i

            i-=1
            if i < 0:
                break

            if nums[i] < nums[i+1]:
                while nums[i] >= nums[min]:
                    min-=1

                t = nums[i]
                nums[i] = nums[min]
                nums[min] = t

                break

        i+=1
        j = len(nums)-1
        while i < j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t

            i+=1
            j-=1

        return nums