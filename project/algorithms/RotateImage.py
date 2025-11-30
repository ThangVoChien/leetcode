from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        leng = len(matrix)
        i = 0
        j = 0

        while j < leng:
            if i == leng:
                break
            if j >= i:
                i+=1
                j = 0
                continue

            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t

            j+=1

        mid = leng / 2
        i = 0
        j = 0
        
        while j < leng:
            if i == leng:
                break
            if j >= mid:
                i+=1
                j = 0
                continue

            t = matrix[i][j]
            matrix[i][j] = matrix[i][leng-1-j]
            matrix[i][leng-1-j] = t

            j+=1

        print(matrix)