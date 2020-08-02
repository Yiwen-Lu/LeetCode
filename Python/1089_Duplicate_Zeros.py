class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for x in arr:
            arr2.append(x)
            if x == 0:
                arr2.append(0)
        arr[:] = arr2[:len(arr)]
        
