from typing import Optional
from dataStructures.LinkedList import ListNode

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng = 0
        node = head
        while node != None:
            node = node.next
            leng+=1

        def divide(head, leng):
            if leng <= 1:
                return head

            n1 = head
            n2 = head

            l = leng
            mid = leng // 2
            while l > mid:
                l-=1
                if l <= mid:
                    t = n2.next
                    n2.next = None
                    n2 = t
                else:
                    n2 = n2.next

            n1 = divide(n1, leng - mid)
            n2 = divide(n2, mid)

            return conquer(n1, n2)

        def conquer(n1, n2):
            if n1 == None or n2 == None:
                return n2 if n1 == None else n1

            head = ListNode(None, n1)
            node = head
            while node.next != None and n2 != None:
                if node.next.val > n2.val:
                    t1 = node.next
                    t2 = n2.next

                    node.next = n2
                    n2.next = t1
                    n2 = t2
                else:
                    node = node.next

            if node.next == None:
                node.next = n2

            return head.next
        
        return divide(head, leng)