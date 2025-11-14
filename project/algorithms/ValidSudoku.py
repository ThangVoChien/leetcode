from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for i in range(9):
            row[i] = set()
            for j in range(9):
                if i == 0:
                    col[j] = set()

                a = (i // 3) * 3 + (j // 3) + 1
                if i % 3 == 0 and j % 3 == 0:
                    box[a] = set()

                x = board[i][j]

                if x == '.':
                    continue
                elif x in row[i] or x in col[j] or x in box[a]:
                    return False
                else:
                    row[i].add(x)
                    col[j].add(x)
                    box[a].add(x)

        return True