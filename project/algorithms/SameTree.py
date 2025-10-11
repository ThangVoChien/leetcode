from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
            
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        if left == False:
            return False
        
        right = self.isSameTree(p.right, q.right)
        if right == False:
            return False
        
        return True