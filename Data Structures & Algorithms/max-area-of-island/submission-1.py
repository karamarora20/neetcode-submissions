class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        vis=[[False for _ in range(c)] for _ in range(r)]
        dir_x=[1,0,-1,0]
        dir_y=[0,1,0,-1]
        def bfs(i,j):
            area=1
            q=deque([(i,j)]) #(x,y,area)
            while(q):
                x,y=q.popleft()
                # print(area)
                for i in range(4):
                    nx=dir_x[i]+x
                    ny=dir_y[i]+y
                    if r>nx>=0 and c>ny>=0 and vis[nx][ny]==False and grid[nx][ny]==1:
                        q.append((nx,ny))
                        vis[nx][ny]=True
                        area+=1
            return area
        ans=0
        for i in range(r):
            for j in range(c):
                if vis[i][j]==False and grid[i][j]==1:
                    vis[i][j]=True
                    ans=max(ans,bfs(i,j))
        return ans
                    
                

