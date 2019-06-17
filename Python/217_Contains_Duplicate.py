class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = set(nums)
        if len(l) == len(nums):
            return False
        else:
            return True