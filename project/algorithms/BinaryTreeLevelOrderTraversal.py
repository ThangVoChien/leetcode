from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        sol = []

        que = []
        que.append(root)
        sol.append([root.val])

        while len(que) != 0:
            s = []

            for n in que:
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)

            if len(s) > 0:
                d = []
                for i in s:
                    d.append(i.val)
                sol.append(d)

            que = s

        return sol

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        sol = []

        que = []
        que.append(root)
        sol.append([root.val])

        while len(que) != 0:
            s = []

            for n in que:
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)

            if len(s) > 0:
                d = []
                for i in s:
                    d.append(i.val)
                sol.append(d)

            que = s

        sol.reverse()
        return sol