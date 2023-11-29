# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

class Solution:
    def __init__(self):
        self.current_pos = []
        self.sol=[]
    def solveNQueens(self, n: int) :
        for i in range(n):
            self.current_pos.append([False for j in range(n)])
        # for i in range(n):
        #     self.current_pos[0][i]=True
        #     self.Solver(n,0,i,[])
        self.Solver(n,0,0)
        print(self.sol)

    #Get current pos using r,c and if we can put Q there add to solution
    def Solver(self,n,r,c):
        if r==n:
            b=[]
            # print(self.current_pos)
            for i in range(len(self.current_pos)):
                buffer_str = ''
                for bool in self.current_pos[i]:
                    if bool:
                        buffer_str=buffer_str+'Q'
                    else:
                        buffer_str=buffer_str+'.'
                b.append(buffer_str)
            self.sol.append(b)
            return
        for col in range(n):
            if self.check_position(n,r,c = col):
                self.current_pos[r][col]=True
                self.Solver(n,r=r+1,c=col)
                self.current_pos[r][col]=False


    def check_position(self,n,r,c):
        #Need to check in the above block weather Q present in U,leftDiagonal, rightDiagonal
        if r==0:
            return True
        #CheckUP
        for i in range(r):
            if self.current_pos[i][c]:
                return False
        #Check leftDiaglonal:
        l_buffer =c
        u_buffer =r
        for i in range(min(r,c)):
            l_buffer=l_buffer-1
            u_buffer=u_buffer-1
            if self.current_pos[u_buffer][l_buffer]:
                return False
        #Check rightDiagonal
        r_buffer = c
        u_buffer = r
        for i in range(min(r,n-c-1)):
            r_buffer = r_buffer+1
            u_buffer = u_buffer-1
            if self.current_pos[u_buffer][r_buffer]:
                return False
        
        return True

        
n=4
a=Solution()
a.solveNQueens(n)

