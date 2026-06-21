from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = sum(v > 0 for row in grid for v in row)
        y = sum(max(col) for col in zip(*grid))
        z = sum(max(row) for row in grid)
        return x + y + z