from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        a = list(range(1, k+1))

        while True:
            sol.append(a[:])

            i = k - 1
            while i >= 0 and a[i] == n - k + i + 1:
                i -= 1

            if i < 0:
                break

            a[i] += 1
            for j in range(i+1, k):
                a[j] = a[j-1] + 1

        return sol