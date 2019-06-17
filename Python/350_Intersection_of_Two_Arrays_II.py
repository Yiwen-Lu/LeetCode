class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        if len(nums1) <= len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        
        for i in nums2:
            if i in nums1:
                l.append(i)
                nums1.remove(i)
        
        return l