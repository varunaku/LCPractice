class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # min_price = prices[0]
        
        # for price in prices:
        #     profit = max(profit, price - min_price)
        #     min_price = min(min_price, price)

        # return profit

        mprofit = 0
        if len(prices) == 1: 
            return mprofit
        l = 0
        r = 1
        while r < len(prices):
            print(l,r, mprofit)
            mprofit = max(prices[r] - prices[l], mprofit)
            if prices[l] > prices[r]:
                l = r
            r += 1
            

        return mprofit
            