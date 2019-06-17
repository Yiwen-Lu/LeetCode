class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if str(x)[0] == '-':
            l = list(str(x))
            l.pop(0)
            l.append('-')
            l.reverse()
            join_list = ''.join(l[:])
            num = int(join_list)
        else:
            num = int(str(x)[::-1])
        
        if num < 2**31-1 and num > -2**31:
            return num
        else:
            return 0