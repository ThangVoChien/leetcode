from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        def backtrack(i, j, arr, length):
            s1 = s[i:j]
            if len(s1) != 0:
                if s1 == s1[::-1]:
                    arr.append(s1)
                    length += len(s1)
                    if length == len(s):
                        sol.append(arr.copy())
                    else:
                        for l in range(j+1, len(s)+1):
                            backtrack(j, l, arr, length)
                    arr.pop()
        for l in range(1, len(s)+1):
            backtrack(0, l, [], 0)
        return sol
    
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_pal[start + 1][end - 1]):
                    is_pal[start][end] = True
        
        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(i):
                    if is_pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]