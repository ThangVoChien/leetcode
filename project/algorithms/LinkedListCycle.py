from typing import Optional, List
from dataStructures.LinkedList import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        while curr != None:
            if curr.val == '':
                return True
            
            curr.val = ''
            curr = curr.next

        return False
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        t = 0
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            t+=1

            if fast == slow:
                break

        slow = head
        if fast != None and fast.next != None:
            while True:
                fast = slow.next
                for j in range(t*2 - 1):
                    if fast == slow:
                        break
                    else:
                        fast = fast.next

                if fast == slow:
                    return slow
                else:
                    slow = slow.next
        else:
            return None