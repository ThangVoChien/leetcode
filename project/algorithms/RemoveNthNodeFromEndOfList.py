from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = ListNode(None, head)
        p2 = p1

        for i in range(n):
            p2 = p2.next

        while p2.next != None:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return head if p1.val != None else p1.next