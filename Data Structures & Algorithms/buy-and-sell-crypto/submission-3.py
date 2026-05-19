class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=0
        max_price=0
        maxx=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[max_price]:
                max_price=i
            if prices[i]<prices[min_price]:
                min_price=i
                max_price=i
            maxx=max(maxx,prices[max_price]-prices[min_price])
        return maxx

