from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(node, s):
            s = s + str(node.val)
            if node.left == None and node.right == None:
                self.sum += int(s)
            else:
                if node.left != None:
                    dfs(node.left, s)
                if node.right != None:
                    dfs(node.right, s)
        dfs(root, "")

        return self.sum