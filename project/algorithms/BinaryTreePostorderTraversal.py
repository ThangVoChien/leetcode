from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def postOrder(node: TreeNode):
            if node == None:
                return
            
            postOrder(node.left)
            postOrder(node.right)
            sol.append(node.val)
        
        postOrder(root)
        return sol