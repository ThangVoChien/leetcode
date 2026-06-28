class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = {chr(i): i - 64 for i in range(ord('A'), ord('Z')+1)}

        sol = 0
        for s in columnTitle:
            sol = sol * 26 + alphabet[s]
        return sol