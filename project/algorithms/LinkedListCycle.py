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
    
def cycleLinkedList(list: List, pos=-1):
    if len(list) == 0:
        return

    head = ListNode(val=list[0])
    node = head
    cycle = node

    for i in range(1, len(list)):
        next = ListNode(val=list[i])
        node.next = next
        node = next

        if i == pos:
            cycle = next

    if pos != -1:
        node.next = cycle

    return head