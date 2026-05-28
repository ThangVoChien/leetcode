from typing import List

class Node:
    def __init__(self, val: int, neighbors: 'Node' = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        if self == None:
            return '[]'
        
        stack = [self]
        set = {self.val: []}

        while len(stack) != 0:
            node = stack.pop()
            for n in node.neighbors:
                set[node.val].append(n.val)
                if n.val not in set:
                    stack.append(n)
                    set[n.val] = []

        s = '['
        for i in sorted(list(set.keys())):
            s += str(sorted(list(set[i])))
            if i != len(set):
                s += ', '
        s += ']'

        return s

def graph(graph: List[List]):
    if graph == None or len(graph) == 0:
        return None

    vertices = [None] * len(graph)
    edges = {i: [] for i in range(1, len(graph)+1)}

    i = 0
    for node in graph:
        vertices[i] = Node(i+1)
        for v in node:
            if vertices[v-1] == None:
                edges[v].append(i+1)
            else:
                vertices[i].neighbors.append(vertices[v-1])
        for e in edges[i+1]:
            vertices[e-1].neighbors.append(vertices[i])
        i+=1

    return vertices[0]