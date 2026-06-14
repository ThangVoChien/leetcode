import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        sol = 0
        st = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                st.append(int(token))
            else:
                a = st.pop()
                b = st.pop()

                if token == '+':
                    sol = (b + a)
                elif token == '-':
                    sol = (b - a)
                elif token == '*':
                    sol = (b * a)
                else:
                    sol = int(b / a)

                st.append(sol)

        return sol