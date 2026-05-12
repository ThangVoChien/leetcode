from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.sol = 0

        self.visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return True
            if (i, j) in self.visited:
                return False

            self.visited.add((i, j))
            if (i-1, j) not in self.visited and dfs(i-1, j):
                self.sol+=1
            if (i, j-1) not in self.visited and dfs(i, j-1):
                self.sol+=1
            if (i+1, j) not in self.visited and dfs(i+1, j):
                self.sol+=1
            if (i, j+1) not in self.visited and dfs(i, j+1):
                self.sol+=1

            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break

        return self.sol