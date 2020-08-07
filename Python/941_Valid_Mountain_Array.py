class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) != 0:
            idx = A.index(max(A))
            if idx == 0 or idx == len(A)-1:
                return False
        else:
            return False
        
        result = True
        for i in range(0, idx-1):
            if A[i] >= A[i+1]:
                result = False
                break
            
        for i in range(idx, len(A)-1):
            if A[i] <= A[i+1]:
                result = False
                break
            
        return result
