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
        startI = 0, startJ = 0
        endI = len(matrix)-1, endJ = len(matrix[0])-1

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