from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol = []

        iBound = 1
        jBound = 1
        next = 1
        horizontal = True

        rowLen = len(matrix)
        colLen = len(matrix[0])
        if colLen == 1:
            horizontal = False

        i = 0
        j = 0
        while True:
            sol.append(matrix[i][j])
            if horizontal:
                j += next
                if j > colLen - iBound or j < iBound - 1:
                    return sol
                if (next == 1 and j == (colLen - iBound)) or (next == -1 and j == (iBound - 1)):
                    horizontal = False
                    if next == -1:
                        jBound+=1
            else:
                i += next
                if i > rowLen - jBound or i < jBound - 1:
                    return sol
                if (next == 1 and i == (rowLen - jBound)) or (next == -1 and i == (jBound - 1)):
                    horizontal = True
                    if next == -1:
                        iBound+=1
                    next = -next

    def generateMatrix(self, n: int) -> List[List[int]]:
        sol = [[0] * n for _ in range(n)]

        iBound = 1
        jBound = 1
        next = 1
        horizontal = True

        i = 0
        j = 0
        x = 1
        while True:
            sol[i][j] = x
            x+=1

            if horizontal:
                j += next
                if j > n - iBound or j < iBound - 1:
                    return sol
                if (next == 1 and j == (n - iBound)) or (next == -1 and j == (iBound - 1)):
                    horizontal = False
                    if next == -1:
                        jBound+=1
            else:
                i += next
                if i > n - jBound or i < jBound - 1:
                    return sol
                if (next == 1 and i == (n - jBound)) or (next == -1 and i == (jBound - 1)):
                    horizontal = True
                    if next == -1:
                        iBound+=1
                    next = -next
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        sol = []
        
        r = 1
        next = 1
        horizontal = True

        i = rStart
        j = cStart
        x = 0
        while True:
            sol.append([i, j])

            if horizontal:
                if abs(j + next - cStart) <= r:
                    j += next
                else:
                    horizontal = False
                    i += next
            else:
                if abs(i + next - rStart) <= r:
                    i += next
                else:
                    if next == -1:
                        r+=1
                    next = -next
                    horizontal = True
                    j += next

            while i >= rows or j >= cols:
                if horizontal:
                    if abs(j + next - cStart) <= r:
                        j += next
                    else:
                        horizontal = False
                        i += next
                else:
                    if abs(i + next - rStart) <= r:
                        i += next
                    else:
                        if next == -1:
                            r+=1
                        next = -next
                        horizontal = True
                        j += next