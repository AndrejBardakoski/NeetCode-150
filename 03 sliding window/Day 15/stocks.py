from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for item in prices:
            min_price = min(min_price, item)
            max_profit = max(max_profit, item - min_price)
        return max_profit
