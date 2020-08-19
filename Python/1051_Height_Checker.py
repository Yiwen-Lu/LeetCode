class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h2 = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != h2[i]:
                count += 1
    
        return count
