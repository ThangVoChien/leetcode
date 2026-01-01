class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[0] * n for _ in range(m)]
        def dynamic(i, j):
            if i == m-1 and j == n-1:
                return 0
            if i == m-1 or j == n-1:
                return 1
            if visited[i][j] != 0:
                return visited[i][j]
            
            visited[i][j] = dynamic(i+1, j) + dynamic(i, j+1)
            return visited[i][j]
        if m == 1 and n == 1:
            return 1
        return dynamic(0, 0)