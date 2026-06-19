from typing import Optional
from dataStructures.LinkedList import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        map = set()
        
        while headA != None and headB != None:
            if headA != None:
                if headA in map:
                    return headA
                else:
                    map.add(headA)
                    headA = headA.next
            
            if headB != None:
                if headB in map:
                    return headB
                else:
                    map.add(headB)
                    headB = headB.next

        return None