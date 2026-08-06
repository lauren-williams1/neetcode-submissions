class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        # create start and end of sliding window
        # create maxProfit to track profit

        # iterate over prices

        # check if the current price is less than the sell price,

        # if not set current price = buy price

        # otherwise calculate maxprofit

        # return maxProfit


        maxProfit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if buy_price > price:
                buy_price = price
            maxProfit = max(maxProfit, price - buy_price)
        
        return maxProfit


        
      
        