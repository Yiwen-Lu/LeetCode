class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        if x < y:
            s1 = list(bin(x)[2:])
            s2 = list(bin(y)[2:])
        else:
            s1 = list(bin(y)[2:])
            s2 = list(bin(x)[2:])
            
        for i in range(len(s2) - len(s1)):
            s1.insert(0, '0')
            
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                count += 1
                
        return count
            
        
        
