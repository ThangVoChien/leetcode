class Solution:
    def hammingWeight(self, n: int) -> int:
        map = {0: 0, 1: 1}
        def divide(n):
            print(n)
            if n in map:
                return map[n]

            b = bin(n).removeprefix('0b')
            map[n] = divide(int(b[:len(b)//2], base=2)) + divide(int(b[len(b)//2:], base=2))

            return map[n]
        return divide(n)