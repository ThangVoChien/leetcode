from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, min, max):
            if node == None:
                return True
            if node.val <= min or node.val >= max:
                return False
            if not dfs(node.left, min, node.val):
                return False
            if not dfs(node.right, node.val, max):
                return False
            return True
        return dfs(root, -2**31-1, 2**31)