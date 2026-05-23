from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        rank = [0] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root2] > rank[root1]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1]+=1

        for e in edges:
            union(e[0], e[1])

        return find(source) == find(destination)