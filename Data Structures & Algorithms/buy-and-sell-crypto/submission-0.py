class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        minP = prices[0]
        for i, price in enumerate(prices):
            minP = min(minP, price)
            k = i + 1
            while k < len(prices):
                if prices[k] < minP:
                    break
                currProfit = prices[k] - minP
                mProfit = max(mProfit, currProfit)
                k+=1
        return mProfit
        