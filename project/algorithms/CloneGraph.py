from typing import Optional
from dataStructures.Graph import Node

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None or node == []:
            return None
        
        stack = [node]
        map = {node.val: Node(node.val)}

        while len(stack) != 0:
            n = stack.pop()
            for i in n.neighbors:
                if i.val not in map:
                    stack.append(i)
                    map[i.val] = Node(i.val)
                map[n.val].neighbors.append(map[i.val])

        return map[1]