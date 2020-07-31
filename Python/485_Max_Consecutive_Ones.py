class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_c = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                if count > max_c:
                    max_c = count
            else:
                count = 0
        return max_c
        
