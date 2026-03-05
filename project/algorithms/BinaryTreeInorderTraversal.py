from typing import List, Optional
from dataStructures.BinaryTree import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def inOrder(node: TreeNode):
            if node == None:
                return
            
            inOrder(node.left)
            sol.append(node.val)
            inOrder(node.right)
        
        inOrder(root)
        return sol