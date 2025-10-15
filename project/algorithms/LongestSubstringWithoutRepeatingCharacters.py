class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        length = 0

        for i in range(len(s)):
            c = s[i]

            dict[c] = i
            if len(dict) > length:
                length = len(dict)
            else:
                if dict[s[i-length]] <= i - length:
                    del dict[s[i-length]]

        return length