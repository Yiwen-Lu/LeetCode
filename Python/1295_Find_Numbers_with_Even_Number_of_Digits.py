class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = []
        count = 0
        for i in nums:
            while (i > 0):
                i = i//10
                count += 1
            digits.append(count)
            count = 0
                
        return len(list(filter(lambda a: a%2 == 0, digits)))
