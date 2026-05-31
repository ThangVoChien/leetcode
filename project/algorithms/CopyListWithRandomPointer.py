from typing import Optional
from dataStructures.LinkedList import ListNode as Node

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        sol = Node(head.val)
        copy = sol

        random = {head: sol}
        if head.random != None:
            if head.random not in random:
                sol.random = Node(head.random.val)
                random[head.random] = sol.random
            else:
                sol.random = random[head.random]
        
        node = head.next
        while node != None:
            n = None
            if node in random:
                n = random[node]
            else:
                n = Node(node.val)
                random[node] = n

            copy.next = n
            copy = copy.next
            
            if node.random != None:
                if node.random not in random:
                    copy.random = Node(node.random.val)
                    random[node.random] = copy.random
                else:
                    copy.random = random[node.random]

            node = node.next

        return sol