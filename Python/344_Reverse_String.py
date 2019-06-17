class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i,k in enumerate(s):
            del s[i]
            s.insert(0, k)
        