from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head
        while list1 != None or list2 != None:
            if list1 == None:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
                continue
            if list2 == None:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
                continue

            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        return head