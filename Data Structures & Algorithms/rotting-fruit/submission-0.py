class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        fruits=0
        rows,cols=len(grid),len(grid[0])
        q=[]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,0))
                if grid[r][c]==1:
                    fruits+=1
        q=deque(q)
        dir_x=[1,0,-1,0]
        dir_y=[0,1,0,-1]
        while(q):
            x,y,t=q.popleft()
            time=max(time,t)
            for i in range(4):
                nx=x+dir_x[i]
                ny=y+dir_y[i]
                if nx>=0 and ny>=0 and nx<rows and ny<cols and grid[nx][ny]==1:
                    q.append((nx,ny,t+1))
                    grid[nx][ny]=2
                    fruits-=1
        return time if fruits==0 else -1
            

