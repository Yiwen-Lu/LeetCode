class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        w = ""
        for i in l:
            w += i[::-1] + " "
            
        return w.strip()
