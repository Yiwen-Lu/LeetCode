class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(set(nums))
        if len(lst) >= 3:
            return lst[-3]
        else:
            return max(lst)
