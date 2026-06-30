from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1, -1, -1):
            n =  target - nums[i]
            if n in nums:
                id = nums.index(n)
                if id != i:
                    numList = list()
                    numList.append(id)
                    numList.append(i)
                    return numList
                
    def twoSum2(self, numbers, target):
        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]

            if sum == target:
                return [start + 1, end + 1]
            elif sum < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        map = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in map:
                return True
            map.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)