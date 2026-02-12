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