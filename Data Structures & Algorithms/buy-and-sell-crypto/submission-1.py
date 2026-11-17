class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        minP = prices[0]
        for price in prices:
            minP = min(minP, price)
            currProfit = price - minP
            mProfit = max(mProfit, currProfit)
        return mProfit
        