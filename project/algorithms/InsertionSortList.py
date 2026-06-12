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
                n = node
                while n != None:
                    n = insertionSort(node.next)
                    if n == None:
                        return None
                    elif node.val != None and n.val < node.val:
                        return n
                    else:
                        n.next = node.next
                        node.next = n
        insertionSort(head)

        return head.next