from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recursion(node):
            if node == None:
                return 0
            elif node.left == None and node.right == None:
                return 1

            left = 10**5
            if node.left != None:
                left = recursion(node.left)

            right = 10**5
            if node.right != None:
                right = recursion(node.right)

            return min(left, right) + 1
        return recursion(root)