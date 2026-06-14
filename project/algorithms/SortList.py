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
            print(head.val, leng)
            if leng <= 1:
                return head

            n1 = head
            n2 = head

            l = leng
            mid = leng // 2
            while l > mid:
                n2 = n2.next
                l-=1

            n1 = divide(n1, mid)
            n2 = divide(n2, leng - mid)

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

                    node = t1
                    n2 = t2
                else:
                    node = node.next

            return head.next
        
        return divide(head, leng)