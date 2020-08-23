class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if rowIndex >= 1:
            for _ in range(rowIndex):
                row.insert(0, 0)
                for j in range(len(row)-1):
                    row[j] = row[j] + row[j+1]
                
        return row
        
