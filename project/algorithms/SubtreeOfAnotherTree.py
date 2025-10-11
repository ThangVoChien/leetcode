from typing import Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        def subtree(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
                
            if p.val != q.val:
                return False
            
            left = subtree(p.left, q.left)
            if left == False:
                return False
            
            right = subtree(p.right, q.right)
            if right == False:
                return False
            
            return True
        
        if root.val == subRoot.val:
            s = subtree(root, subRoot)
            if s:
                return True
        
        left = self.isSubtree(root.left, subRoot)
        if left == True:
            return True
        
        right = self.isSubtree(root.right, subRoot)
        if right == True:
            return True

        return left or right