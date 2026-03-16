from typing import List, Optional
from dataStructures.BinaryTree import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        sol = []

        que = []
        que.append(root)
        sol.append([root.val])

        rev = True
        while len(que) != 0:
            s = []

            for n in que:
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)

            if len(s) > 0:
                d = []
                if rev:
                    for i in range(len(s)-1, -1, -1):
                        d.append(s[i].val)
                else:
                    for i in range(len(s)):
                        d.append(s[i].val)
                sol.append(d)
                rev = not rev

            que = s

        return sol