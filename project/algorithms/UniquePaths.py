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
        visited = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        def dynamic(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1
            if visited[i][j] != 0:
                return visited[i][j]
            
            if i == len(obstacleGrid)-1:
                visited[i][j] = dynamic(i, j+1)
            elif j == len(obstacleGrid[0])-1:
                visited[i][j] = dynamic(i+1, j)
            else:
                visited[i][j] = dynamic(i+1, j) + dynamic(i, j+1)
            return visited[i][j]
        return dynamic(0, 0)