class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = last_max = nums[0]
        for i in range(1, len(nums)):
            max_sub = max(max_sub + nums[i], nums[i])
            last_max = max(last_max, max_sub)
        return last_max