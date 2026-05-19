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
    
    def maxProfit3(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for i in range(1, len(prices)):
            price = prices[i]

            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        
        return sell2