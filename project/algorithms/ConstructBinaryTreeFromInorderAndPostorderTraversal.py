from typing import List, Optional
from dataStructures.BinaryTree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.order = {val: index for index, val in enumerate(inorder)}

        def divide(start, end):
            if len(postorder) == 0 or start > end:
                return None
            
            node = TreeNode(postorder.pop())
            mid = self.order[node.val]

            node.right = divide(mid+1, end)
            node.left = divide(start, mid-1)

            return node
        
        return divide(0, len(inorder)-1)