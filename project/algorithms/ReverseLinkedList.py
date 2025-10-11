from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        reversed = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return reversed
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == 1:
            return head
        
        left-=1
        right-=1
        reversed = self.reverseBetween(head.next, left, right)
        
        tail = reversed
        if left < 1:
            tail = head.next.next
            head.next.next = head
        head.next = tail

        return reversed if left < 1 else head