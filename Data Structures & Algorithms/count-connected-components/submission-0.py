class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis=set([])
        def bfs(start):
            q=deque([start])
            while(q):
                curr=q.popleft()
                for nei in g[curr]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append(nei)
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        cnt=0
        for i in range(n):
            if i not in vis:
                vis.add(i)
                bfs(i)
                cnt+=1
        return cnt
        