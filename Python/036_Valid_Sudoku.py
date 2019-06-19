class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """        
        # check row
        for i in range(len(board)):
            row_num = []
            for j in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] in row_num:
                        return False
                    else:
                        row_num.append(board[i][j])
        
        # check col
        for j in range(len(board)):
            col_num = []
            for i in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] in col_num:
                        return False
                    else:
                        col_num.append(board[i][j])
                        
        # check 3x3
        for i in range(0, len(board)-2, 3):
            for j in range(0, len(board)-2, 3):
                if (i%3 == 0) & (j%3 == 0):
                    sub_box = []
                    for a in range(3):
                        for b in range(3):
                            if board[i+a][j+b].isdigit():
                                if board[i+a][j+b] in sub_box:
                                    return False
                                else:
                                    sub_box.append(board[i+a][j+b])
                        
        return True
        
