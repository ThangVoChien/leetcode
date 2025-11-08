from typing import Optional
from dataStructures.BinaryTree import TreeNode
from dataStructures.LinkedList import ListNode
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced

            if root == None or not balanced:
                return 0
            
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            if abs(left - right) > 1:
                balanced = False
                return 0

            return left if left >= right else right
        dfs(root)
        return balanced
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = deque()
        st2 = deque()

        l = l1
        while l != None:
            st1.append(l)
            l = l.next

        l = l2
        while l != None:
            st2.append(l)
            l = l.next

        flag = None
        if len(st1) >= len(st2):
            sol = st1
            add = st2
            flag = True
        else:
            sol = st2
            add = st1
            flag = False

        r = 0
        s = None
        while len(sol) > 0 and len(add) > 0:
            s = sol.pop()
            a = add.pop()

            s.val += a.val

            if r > 0:
                s.val += 1
                r = 0

            if s.val >= 10:
                s.val -= 10
                r = 1

        while r == 1:
            if len(sol) > 0:
                s = sol.pop()
                s.val += 1

                if s.val >= 10:
                    s.val -= 10
                    r = 1
                else:
                    r = 0
            else:
                return ListNode(1, s)
            
        return l1 if flag else l2