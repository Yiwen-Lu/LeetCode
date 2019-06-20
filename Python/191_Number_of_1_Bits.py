class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return sum([int(x) for x in list(str(n))])
        
        str_n = bin(n)[2:]
        return str_n.count('1')

