class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        q=[]
        for r in [0,rows-1]:
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='#'
                    q.append((r,c))
        for c in [0,cols-1]:
            for r in range(1,rows-1):
                  if board[r][c]=='O':
                    board[r][c]='#'
                    q.append((r,c))
        q=deque(q)
        dir_x=[1,0,-1,0]
        dir_y=[0,1,0,-1]
        while(q):
            x,y=q.popleft()
            for i in range(4):
                nx=x+dir_x[i]
                ny=y+dir_y[i]
                if nx>=0 and ny>=0 and nx<rows and ny<cols and board[nx][ny]=='O':
                    q.append((nx,ny))
                    board[nx][ny]='#'
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='#':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
                
            

