class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]

        maxProfit = 0


        for price in prices[1:]:
            if buy_price > price:
                buy_price = price
            
            maxProfit = max(maxProfit, price - buy_price)
        
        return maxProfit

      
        