class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        vis=[[False for _ in range(c)] for _ in range(r)]
        def bfs(i,j):
            q=deque([(i,j)])
            while(q):
                x,y=q.popleft()
                vis[x][y]=True
                dir_x=[1,0,-1,0]
                dir_y=[0,1,0,-1]
                for i in range(4):
                    nx=dir_x[i]+x
                    ny=dir_y[i]+y
                    if r>nx>=0 and c>ny>=0 and grid[nx][ny]=='1' and vis[nx][ny]==False:
                        q.append((nx,ny))
        ans=0
        for i in range(r):
            for j in range(c):
                if not vis[i][j] and grid[i][j]=='1':
                    bfs(i,j)
                    ans+=1
        return ans
                    

