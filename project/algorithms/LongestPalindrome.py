class Solution:
    def longestPalindrome(self, s: str) -> int:
        sol = 0

        map = {}
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        odd = 0
        for v in map.values():
            if odd == 0 and v % 2 == 1:
                odd = 1
            sol += v // 2 * 2

        return sol + odd