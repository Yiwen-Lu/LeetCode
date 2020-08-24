class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            try:
                j = numbers.index(target - numbers[i])
                if i == j:
                    l = nums[i:]
                    j = l.index(target - numbers[i]) + i
                break
            except:
                continue
                
        return [i + 1, j + 1]
        
