class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        substr = ""

        for i in range(len(s)):
            if i != 0 and s[i] == s[i-1]:
                continue

            start = i
            end = i + 1

            while end < len(s) - 1 and s[start] == s[end] and s[start] == s[end+1]:
                end+=1

            if end < len(s) and s[start] != s[end]:
                start -= 1
            
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            if start == end - 1:
                start-=1

            ln = end - start - 1
            if length < ln:
                length = ln
                substr = s[start+1:end]

        return substr