class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for _ in range(n)] for _ in range(n)]
        ans=[]
        def check(row,col,board):
            r=row-1
            while(r>=0):
                if board[r][col]=='Q':
                    return False
                r-=1
            r,c=row-1,col-1
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r,c=row-1,col+1
            while r>=0 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            return True
                
            
            
        def n_queen(r):
            if r==n:
                copy=["".join(row) for row in board]
                ans.append(copy)
                return
            else:
    
                for c in range(n):
                    if  check(r,c,board):
                        board[r][c]='Q'
                        n_queen(r+1)
                        board[r][c]='.'
        n_queen(0)
        return ans



