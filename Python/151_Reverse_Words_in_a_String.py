class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        w = ""
        for i in reversed(l):
            w += i + " "
            
        return w.strip()
