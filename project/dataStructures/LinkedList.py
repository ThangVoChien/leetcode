from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self == None:
            return '[]'
        
        map = set()
        node = self

        s = '['
        while node != None and node not in map:
            s += str(node.val)
            if node != None:
                if node.next not in map:
                    s += ', '
                else:
                    s += '; ' + str(node.next.val)

            map.add(node)
            node = node.next
        s += ']'

        return s

def linkedList(list: List, pos = -1):
    if list == None or len(list) == 0:
        return None
    
    head = ListNode(val=list[0])
    node = head
    cycle = None

    for i in range(1, len(list)):
        next = ListNode(val=list[i])
        node.next = next
        node = next

        if i == pos:
            cycle = next
    node.next = cycle

    return head