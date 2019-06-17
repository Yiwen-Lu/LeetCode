class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dir = {}
        for i in s:
            s_dir[i] = s_dir.get(i, 0) + 1
            
        for i,k in enumerate(s):
            if s_dir[k] == 1:
                return i
            
        return -1
