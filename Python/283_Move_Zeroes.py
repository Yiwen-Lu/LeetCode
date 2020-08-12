class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        """
        # Method 1:
        count = nums.count(0)
        
        for _ in range(count):
            nums.remove(0)
            nums.append(0)
            
        return nums
        """
    
        """
        # Method 2:
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        """
    
        z = nums.count(0)
        nums[:(len(nums)-z)] = list(filter(lambda a: a != 0, nums)) 
        if z != 0:
            nums[-z:] = [0 for _ in range(z)]
    
