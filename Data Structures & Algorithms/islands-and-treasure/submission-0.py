class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        m, n = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647
        
        # Step 1: Add all treasure cells (0) to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    # Only update unvisited land cells (INF)
                    if grid[nx][ny] == INF:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx, ny))