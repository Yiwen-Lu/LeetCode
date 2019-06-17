class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
        
        else:
            for i in reversed(range(len(digits))):
                if digits[i] == 9:
                    digits[i] = 0
                elif digits[i] != 9:
                    digits[i] += 1
                    break
            
            if digits[0] == 0:
                digits[0] = 1
                
            if set(digits) == {0, 1} or set(digits) == {1}:
                digits.append(0)
            

        return digits