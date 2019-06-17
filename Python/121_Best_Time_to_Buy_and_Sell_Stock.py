class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
            else:
                gap = max(prices[i:]) - lowest
                if profit < gap:
                    profit = gap
        return profit
        