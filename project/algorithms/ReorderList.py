from typing import Optional
from dataStructures.LinkedList import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        
        node = head
        while node != None:
            stack.append(node)
            node = node.next

        if len(stack) < 3:
            return

        node = head
        while True:
            t = node.next
            node.next = stack.pop()
            node.next.next = t
            node = t

            if node == stack[-1]:
                node.next = None
                break
            elif node.next == stack[-1]:
                node.next.next = None
                break