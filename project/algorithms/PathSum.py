from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum):
            if node == None:
                return False
            
            sum += node.val
            if sum == targetSum and node.left == None and node.right == None:
                return True
            
            return dfs(node.left, sum) or dfs(node.right, sum)
        return dfs(root, 0)