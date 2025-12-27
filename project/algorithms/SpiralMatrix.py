from typing import List, Optional
from dataStructures.LinkedList import ListNode

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

            t = 0
            while i < 0 or j < 0 or i >= rows or j >= cols:
                if t == 3:
                    return sol
                
                if i < 0 or i >= rows:
                    horizontal = False

                    if i < 0:
                        r+=1
                        next = 1
                        i = 0
                    else:
                        next = -1
                        i = rows-1
                    j = cStart + next * r
                else:
                    horizontal = True

                    if j < 0:
                        next = 1
                        j = 0
                    else:
                        next = -1
                        j = cols-1
                    i = rStart + -next * r
                    
                    if j == 0 and i >= 0 and next == 1:
                        r+=1

                t+=1

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        sol = [[-1] * n for _ in range(m)]

        iBound = 1
        jBound = 1
        next = 1
        horizontal = True
        if n == 1:
            horizontal = False

        i = 0
        j = 0
        while True:
            sol[i][j] = head.val
            head = head.next
            if head == None:
                return sol

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
                if i > m - jBound or i < jBound - 1:
                    return sol
                if (next == 1 and i == (m - jBound)) or (next == -1 and i == (jBound - 1)):
                    horizontal = True
                    if next == -1:
                        iBound+=1
                    next = -next