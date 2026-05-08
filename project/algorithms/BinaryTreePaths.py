from typing import List, Optional

from dataStructures.BinaryTree import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        sol = []
        
        def backtrack(node, l):
            if node == None:
                return
            
            l.append(str(node.val))
            
            if node.left == None and node.right == None:
                sol.append("->".join(l))
            else:
                backtrack(node.left, l)
                backtrack(node.right, l)
            
            l.pop()
        backtrack(root, [])
        
        return sol