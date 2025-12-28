from typing import List

class ListNode:
    def __init__(self, val=0, next=None, cycle=False):
        self.val = val
        self.next = next
        self.__cycle = cycle

    def __str__(self):
        if self == None:
            return '[]'
        
        node = self
        cycle = None
        i = 0

        s = '['
        while node != None and node != cycle:
            if node._ListNode__cycle:
                cycle = node
            if cycle == None:
                i+=1

            s += str(node.val)
            node = node.next
            if node != None and node != cycle:
                s += ', '
        s += ']'

        if cycle != None:
            s += ', pos = ' + str(i)

        return s

def linkedList(list: List, pos = -1):
    head = ListNode(val=list[0])
    node = head
    cycle = None

    for i in range(1, len(list)):
        next = ListNode(val=list[i])
        node.next = next
        node = next

        if i == pos:
            cycle = next
            cycle._ListNode__cycle = True

    if cycle != None:
        node.next = cycle

    return head