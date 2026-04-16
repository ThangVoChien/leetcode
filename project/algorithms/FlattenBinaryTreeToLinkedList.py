from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if node == None or (node.right == None and node.left == None):
                return node

            r = dfs(node.right)
            l = dfs(node.left)

            if l != None:
                t = node.right
                node.right = node.left
                l.right = t
                node.left = None

            return r if r != None else l
        dfs(root)

        return root