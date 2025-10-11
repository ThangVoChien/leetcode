from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        t = root.left
        root.left = root.right
        root.right = t

        return root