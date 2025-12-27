from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self == None:
            return '[]'
        
        s = '['
        node = self
        while node != None:
            s += str(node.val)
            if node.next != None:
                s += ', '
            node = node.next
        s += ']'
        return s

def linkedList(list: List, pos = -1):
    head = ListNode(val=list[0])
    node = cycle = head

    for i in range(1, len(list)):
        next = ListNode(val=list[i])
        node.next = next
        node = next

        if i == pos:
            cycle = next

    if pos != -1:
        node.next = cycle

    return head