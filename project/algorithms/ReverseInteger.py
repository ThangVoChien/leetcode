class Solution:
    def reverse(self, x: int) -> int:
        max = 2**31 - 1
        min = -2**31

        sign = 1 if x >= 0 else -1
        x = abs(x)

        y = 0
        while x != 0:
            a = x % 10
            x //= 10

            if (sign == 1 and max / 10 < y + (a / 10)) or (sign == -1 and -(min / 10) < y + (a / 10)):
                return 0

            y *= 10
            y += a

        return sign * y