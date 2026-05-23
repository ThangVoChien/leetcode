from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def check(i, j, v):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if (i, j) in v or board[i][j] == 'X':
                return True
            v.add((i, j))
            visited.add((i, j))
            return check(i-1, j, v) and check(i, j+1, v) and check(i+1, j, v) and check(i, j-1, v)
        
        def mod(i, j, v):
            if (i, j) in v or board[i][j] == 'X':
                return
            else:
                board[i][j] = 'X'
                v.add((i, j))
            mod(i-1, j, v) or mod(i, j+1, v) or mod(i+1, j, v) or mod(i, j-1, v)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited and check(i, j, set()):
                    mod(i, j, set())