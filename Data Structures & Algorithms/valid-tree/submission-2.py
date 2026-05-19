class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        q=deque([(0,-1)])
        vis=set([0])
        while(q):
            curr,parent=q.popleft()
            for nei in g[curr]:
                if nei==parent:
                    continue
                if nei in vis:
                    return False
                vis.add(nei)
                q.append((nei,curr))
        return len(vis)==n