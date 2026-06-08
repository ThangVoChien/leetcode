from typing import Optional
from dataStructures.LinkedList import ListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, head)
        def insertionSort(node):
            if node.next == None:
                return None
            
            if node.val != None and node.val > node.next.val:
                next = node.next
                node.next = next.next
                return next
            else:
                n = insertionSort(node.next)
                
                if n == None:
                    return None
                elif n.val < node.val:
                    return n
                else:
                    n.next = node.next
                    node.next = n

        node = insertionSort(head)
        while node != None:
            node = insertionSort(node)

        return head.next