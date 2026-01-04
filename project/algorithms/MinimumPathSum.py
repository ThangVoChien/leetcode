from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = [[-1] * len(grid[0]) for _ in range(len(grid))]
        def dynamic(i, j):
            if i == len(grid) or j == len(grid[0]):
                return 999999999
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            if visited[i][j] != -1:
                return visited[i][j]
            
            visited[i][j] = min(dynamic(i+1, j) + grid[i][j], dynamic(i, j+1) + grid[i][j])
            print(visited[i][j])
            return visited[i][j]
        return dynamic(0, 0)