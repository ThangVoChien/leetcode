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

def linkedList(list: List = []):
    if len(list) == 0:
        return

    head = ListNode(val=list[0])
    node = head

    for i in range(1, len(list)):
        next = ListNode(val=list[i])
        node.next = next
        node = next

    return head