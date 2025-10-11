from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        reversed = Solution().reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed