from typing import List, Optional
from dataStructures.BinaryTree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.order = {val: index for index, val in enumerate(inorder)}

        def divide(start, end):
            if len(preorder) == 0 or start > end:
                return None
            
            node = TreeNode(preorder.pop(0))
            mid = self.order[node.val]

            node.left = divide(start, mid-1)
            node.right = divide(mid+1, end)

            return node
        
        return divide(0, len(inorder)-1)