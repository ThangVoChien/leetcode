from typing import Optional
from dataStructures.LinkedList import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start = ListNode(0, None)
        end = ListNode(0, None)
        headStart = start
        headEnd = end

        while head != None:
            if head.val < x:
                start.next = head
                start = start.next
            else:
                end.next = head
                end = end.next
            head = head.next

        start.next = headEnd.next
        end.next = None
        return headStart.next