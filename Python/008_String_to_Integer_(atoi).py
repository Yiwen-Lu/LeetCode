class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ""
        for i in str:
            if (i == "-" or i == "+") and num == "":
                num += i
            elif i.isnumeric():
                num += i
            elif i == ".":
                break
            elif i == " " and num == "":
                continue
            else:
                break
        
        try:
            num = int(num)

            if num > (2 ** 31 - 1):
                return 2 ** 31 - 1
            elif num < -(2 ** 31 -1):
                return -(2 ** 31)

            else:
                return num
        except:
            return 0
