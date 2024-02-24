class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 10010
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit