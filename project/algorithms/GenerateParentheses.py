from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        s = set()

        def backtrack(str, idx, num):
            str = str[:idx+1] + '()' + str[idx+1:]

            if str not in s:
                s.add(str)

                if num == n:
                    sol.append(str)
                else:
                    for i in range(-1, len(str)+1):
                        if i == -1 or i == len(str) or str[i] == '(':
                            backtrack(str, i, num+1)

        backtrack("", -1, 1)

        return sol