from typing import Optional

from dataStructures.BinaryTree import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left == None or right == None:
                return left == right
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root, root)