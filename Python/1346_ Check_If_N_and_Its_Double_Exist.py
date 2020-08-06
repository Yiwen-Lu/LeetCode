class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        double = False
        arr2 = []
        for idx,num in enumerate(arr):
            arr2[:] = arr[:]
            arr2.pop(idx)
            if (num*2 in arr2):
                double = True
                return double
            
        return double
