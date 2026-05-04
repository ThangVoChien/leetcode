class Solution:
    def reverseBits(self, n: int) -> int:
        rev = bin(n).removeprefix('0b')[::-1]
        rev += (32 - len(rev)) * '0'
        return int(rev, base=2)