class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = [chr(c) for c in range(ord('A'), ord('Z')+1)]
        sol = []
        
        d = columnNumber
        while d != 0:
            r = d % 26
            d //= 26

            sol.append(alphabet[r-1])
            if r == 0:
                d-=1
        return "".join(sol[::-1])