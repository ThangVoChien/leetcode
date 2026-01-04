from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[0] * n for _ in range(m)]
        def dynamic(i, j):
            if i == m-1 or j == n-1:
                return 1
            if visited[i][j] != 0:
                return visited[i][j]
            
            visited[i][j] = dynamic(i+1, j) + dynamic(i, j+1)
            return visited[i][j]
        return dynamic(0, 0)
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        visited = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        def dynamic(i, j):
            if i == len(obstacleGrid) or j == len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1
            if visited[i][j] != -1:
                return visited[i][j]
            
            visited[i][j] = dynamic(i+1, j) + dynamic(i, j+1)
            return visited[i][j]
        return dynamic(0, 0)
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        leng = 0
        start = tuple()

        def backtrack(i, j, v: list):
            if i == -1 or i == len(grid) or j == -1 or j == len(grid[0]) or grid[i][j] == -1 or (i, j) in v:
                return 0
            
            v.append((i, j))
            if grid[i][j] == 2:
                if len(v) != leng:
                    v.pop()
                    return 0
                else:
                    v.pop()
                    return 1
            
            sol = backtrack(i-1, j, v) + backtrack(i, j+1, v) + backtrack(i+1, j, v) + backtrack(i, j-1, v)
            v.pop()
            return sol

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == -1:
                    continue
                if grid[i][j] == 1:
                    start = (i, j)
                leng+=1
        
        return backtrack(start[0], start[1], [])