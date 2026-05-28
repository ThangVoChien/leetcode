from typing import List

class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None, random: 'ListNode' = None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        if self == None:
            return '[]'
        
        map = set()
        node = self

        s = '['
        n = ''
        while node != None and node not in map:
            if node.random != None:
                n = '[' + str(node.val) + '; ' + str(node.random.val) + ']'
            else:
                n = str(node.val)
            s += n

            if node != None and node.next != None:
                if node.next not in map:
                    s += ', '
                else:
                    s += '; ' + str(node.next.val)

            map.add(node)
            node = node.next
        s += ']'

        return s

def linkedList(list: List, pos: int = -1):
    if list == None or len(list) == 0:
        return None
    
    if isinstance(list[0], List):
        head = ListNode(list[0][0])
    else:
        head = ListNode(list[0])
    node = head
    cycle = None
    random = {0: head}

    for i in range(1, len(list)):
        if isinstance(list[i], List):
            if i in random:
                next = random[i]
            else:
                next = ListNode(list[i][0])
                random[i] = next

            if list[i-1][1] != None:
                if list[i-1][1] not in random:
                    random[list[i-1][1]] = ListNode(list[list[i-1][1]][0])
                node.random = random[list[i-1][1]]
        else:
            next = ListNode(list[i])
        node.next = next
        node = next

        if i == pos:
            cycle = next
    
    node.next = cycle
    if isinstance(list[i], List):
        node.random = random[list[len(list)-1][1]]

    return head