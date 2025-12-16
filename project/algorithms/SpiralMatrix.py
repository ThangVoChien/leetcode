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