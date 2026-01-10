class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n)]
        def dynamic(i):
            if i == 1 or i == 2:
                return i
            if memo[i-1] != 0:
                return memo[i-1]

            memo[i-1] = dynamic(i-1) + dynamic(i-2)
            return memo[i-1]
        return dynamic(n)