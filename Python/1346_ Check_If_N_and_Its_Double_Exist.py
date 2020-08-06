class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr2 = []
        for idx,num in enumerate(arr):
            arr2[:] = arr[:]
            arr2.pop(idx)
            if (num*2 in arr2):
                return True
                break
            
        return False
