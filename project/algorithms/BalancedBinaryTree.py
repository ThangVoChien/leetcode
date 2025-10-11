from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced

            if root == None or not balanced:
                return 0
            
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            if abs(left - right) > 1:
                balanced = False
                return 0

            return left if left >= right else right
        dfs(root)
        return balanced