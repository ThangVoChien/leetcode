from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        h = head.next

        def swap(node, prev):
            if node == None or node.next == None:
                return
            
            next = node.next.next

            if prev != None:
                prev.next = node.next    
            node.next.next = node
            node.next = next

            swap(next, node)

        swap(head, None)

        return h
