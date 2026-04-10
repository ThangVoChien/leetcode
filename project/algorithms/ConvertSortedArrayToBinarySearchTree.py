from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(start, end):
            if end < start:
                return None
            
            mid = int((start + end) / 2)
            node = TreeNode(nums[mid])

            node.left = divide(start, mid-1)
            node.right = divide(mid+1, end)

            return node
        return divide(0, len(nums)-1)