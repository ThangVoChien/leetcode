from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = (2**31) - 1
        profit = 0

        for price in prices:
            if price > buyPrice:
                p = price - buyPrice
                profit = max(p, profit)
            if price < buyPrice:
                buyPrice = price

        return profit
    
    def maxProfit2(self, prices: List[int]) -> int:
        buyPrice = (2**31) - 1
        profit = 0
        
        for price in prices:
            if price > buyPrice:
                profit += price - buyPrice
                buyPrice = (2**31) - 1
            if price < buyPrice:
                buyPrice = price

        return profit