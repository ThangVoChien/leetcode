from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr != None:
            while curr.next != None and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next

        return head
    
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(None, head)
        curr = head

        prev = h
        while curr != None:
            p = prev
            while curr != None and (p.val == curr.val or (curr.next != None and curr.val == curr.next.val)):
                p = curr
                curr = curr.next
            prev.next = curr
            prev = prev.next
            if curr != None:
                curr = curr.next

        return h.next