from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break
        
        return dp[-1]
    
    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []

        def dfs(pref: str, suff: str)-> None:
            if suff == '':
                ans.append(pref.rstrip())    
            else:
                for i in range(len(suff)):
                    if suff[:i+1] not in wordDict: continue
                    dfs(pref + suff[:i+1]+ ' ', suff[i+1:])
        dfs('', s)

        return ans