from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2

            i = mid // len(matrix[0])
            j = mid - i * len(matrix[0])

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
    
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        def divideConquer(startI, endI, startJ, endJ):
            print(startI, endI, startJ, endJ)
            if startI > endI or startJ > endJ:
                return False
            if startI == endI and startJ == endJ:
                mid = (startI + endI) // 2
                return matrix[mid][mid] == target

            midI = (startI + endI) // 2
            midJ = (startJ + endJ) // 2

            if matrix[midI][midJ] == target:
                return True
            elif matrix[midI][midJ] > target:
                return divideConquer(startI, midI, startJ, midJ)
            else:
                if startI == endI:
                    return divideConquer(startI, midI, midJ+1, endJ)
                elif startJ == endJ:
                    return divideConquer(midI+1, endI, startJ, endJ)
                return divideConquer(midI+1, endI, startJ, endJ) or divideConquer(startI, midI, midJ+1, endJ)
        return divideConquer(0, len(matrix)-1, 0, len(matrix[0])-1)