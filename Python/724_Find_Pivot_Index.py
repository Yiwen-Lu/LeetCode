class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                result = i
                break
                
        return result
