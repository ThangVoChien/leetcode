from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = (2**31) - 1
        sellPrice = 0
        profit = 0

        for price in prices:
            if price < buyPrice:
                buyPrice = price
                sellPrice = 0
                continue
            if price > sellPrice:
                sellPrice = price
                p = sellPrice - buyPrice
                profit = max(p, profit)

        return profit