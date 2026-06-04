from typing import List, Optional
from dataStructures.BinaryTree import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def preOrder(node: TreeNode):
            if node == None:
                return
            
            sol.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return sol