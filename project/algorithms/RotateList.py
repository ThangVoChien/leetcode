from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head

        tail = head
        back = 0

        i = 0
        while i < k:
            if tail.next == None:
                tail = head
                back = k % (i+1)
                if back == 0:
                    return head
                break
            tail = tail.next
            i+=1

        j = 0
        while j < back:
            tail = tail.next
            j+=1

        curr = head
        while tail.next != None:
            curr = curr.next
            tail = tail.next

        tail.next = head
        head = curr.next
        curr.next = None

        return head