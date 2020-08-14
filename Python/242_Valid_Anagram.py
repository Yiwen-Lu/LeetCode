class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = sorted([i for i in s])
        lt = sorted([j for j in t])
        if ls == lt:
            return True
        else:
            return False
