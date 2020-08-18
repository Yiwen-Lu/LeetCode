class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        result = nums.index(m)
        for x in nums:
            if (x != m) & (2 * x > m):
                result = -1
        
        return result
