class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        
        zigzag = ""

        for i in range(numRows, 0, -1):
            down = True
            j = numRows - i

            while j < len(s):
                zigzag += s[j]

                next = 0
                while next == 0:
                    if down:
                        next = (i - 1) * 2
                    else:
                        next = (numRows - i) * 2
                    down = not down

                j += next

        return zigzag