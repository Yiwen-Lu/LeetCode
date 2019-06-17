class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            gap = prices[i+1] - prices[i]
            if gap > 0:
                profit += gap
        return profit