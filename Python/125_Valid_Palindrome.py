class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = (''.join(e for e in s if e.isalnum())).lower()
        result = True
        
        for i in range(len(t)):
            if t[i] != t[-i-1]:
                result = False
                break
                
        return result
