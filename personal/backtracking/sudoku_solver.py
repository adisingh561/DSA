# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.


#### TO BE DONE AGAIN ####


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        #Modify board if solution not good revert board to the original
        self.solver(board,0,0)
    
    def solver(self,board,r,c):
        if r==9 and c == 9:
            return
        
        for num in range(10):
            if self.isSafe(board,r,c,num):
                board[r][c] = str(num)
                self.solver(board,r,c+1)
        
        

    def isSafe(self,board,r,c,num):
        #Check num in row 
        if num in board[r]:
            return False
        #Check num in column
        for i in range(10):
            if board[i][c]==num:
                return False
        #Check in the 3x3 block
        #So starting pos of block
        s_r=r-r%3
        s_c=c-c%3
        for i in range(3):
            for j in range(3):
                if board[s_r+i][s_c+j]==num:
                    return False
        return True
a = Solution()
a.solveSudoku(board)