from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        map = set()
        self.max = 0

        parent = {n: n for n in nums}
        size = {n: 1 for n in nums}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if size[root1] >= size[root2]:
                    parent[root2] = root1
                    size[root1] += size[root2]
                    if size[root1] > self.max:
                        self.max = size[root1]
                else:
                    parent[root1] = root2
                    size[root2] += size[root1]
                    if size[root2] > self.max:
                        self.max = size[root2]

        for n in nums:
            if n-1 in map:
                union(n-1, n)
            if n+1 in map:
                union(n, n+1)
            map.add(n)

        return self.max