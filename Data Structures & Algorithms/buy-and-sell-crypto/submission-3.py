class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l,r = 0,1

        while r<len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                max_profit = max(max_profit, profit)

            else:
                l = r
            r += 1
        

        # max_profit = 0 

        # lowest = prices[0]

        # for price in prices:
        #     if price<lowest:
        #         lowest = price
        #     max_profit = max(max_profit, price - lowest)
        
        return max_profit

