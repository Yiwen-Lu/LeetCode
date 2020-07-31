class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        sqr_A = []
        for i in A:
            sqr_A.append(i**2)
        return sorted(sqr_A)
