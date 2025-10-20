class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        n = 0
        sign = 1
        curr = 0

        while curr < len(s) and s[curr] == " ":
            curr+=1

        if curr >= len(s):
            return 0
        elif s[curr] == "-" or s[curr] == "+":
            if s[curr] == "-":
                sign = -1
            curr+=1

        while curr < len(s):
            if not s[curr].isnumeric():
                break

            n *= 10
            n += int(s[curr])

            curr+=1

        n = n * sign
        if n < -2**31:
            n = -2**31
        elif n > 2**31 - 1:
            n = 2**31 - 1

        return n