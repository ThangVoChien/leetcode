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