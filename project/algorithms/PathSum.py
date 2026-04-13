from typing import List, Optional
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
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.sol = []

        def dfs(node, sum, list):
            if node == None:
                return
            
            sum += node.val
            list.append(node.val)

            if sum == targetSum and node.left == None and node.right == None:
                self.sol.append(list.copy())
            else:
                if node.left != None:
                    dfs(node.left, sum, list)
                if node.right != None:
                    dfs(node.right, sum, list)

            list.pop()
        dfs(root, 0, [])
        
        return self.sol