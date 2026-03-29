from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []

        self.chess = [("." * n) for _ in range(n)]
        
        self.hor = [True for _ in range(n)]
        self.diaI = [True for _ in range(2*n-1)]
        self.diaJ = [True for _ in range(2*n-1)]

        def generate(i):
            for j in range(n):
                if self.hor[j] and self.diaI[n-1-i+j] and self.diaJ[j+i]:
                    self.chess[i] = (("." * j) + "Q" + ("." * (n-j-1)))

                    self.hor[j] = False
                    self.diaI[n-1-i+j] = False
                    self.diaJ[j+i] = False

                    if i == n-1:
                        sol.append(self.chess.copy())
                    else:
                        generate(i+1)

                    self.hor[j] = True
                    self.diaI[n-1-i+j] = True
                    self.diaJ[j+i]  = True
        generate(0)

        return sol