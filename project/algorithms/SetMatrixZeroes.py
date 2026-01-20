from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = False
        col = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            if col:
                for i in range(1, len(matrix)):
                    matrix[i][0] = 0
            if row:
                for j in range(1, len(matrix[0])):
                    matrix[0][j] = 0