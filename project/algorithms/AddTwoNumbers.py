from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0

        i = 1
        while l1 != None or l2 != None:
            if l1 != None:
                n1 += l1.val * i
                l1 = l1.next

            if l2 != None:
                n2 += l2.val * i
                l2 = l2.next

            i *= 10

        n3 = n1 + n2
        l3 = ListNode(n3 % 10)
        n3 //= 10

        l = l3
        while n3 != 0:
            n = ListNode(n3 % 10)
            n3 //= 10

            l.next = n
            l = l.next

        return l3