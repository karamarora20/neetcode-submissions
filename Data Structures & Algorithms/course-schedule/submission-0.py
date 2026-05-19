class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[] for _ in range(numCourses)]
        in_deg=[0 for _ in range(numCourses)]
        for v,u in prerequisites:
            g[u].append(v)
            in_deg[v]+=1
        q=deque([])
        for i in range(numCourses):
            if in_deg[i]==0:
                q.append(i)
        order=[]
        while(q):
            curr=q.popleft()
            order.append(curr)
            for nei in g[curr]:
                in_deg[nei]-=1
                if in_deg[nei]==0:
                    q.append(nei)
        if len(order)!=numCourses:
            return False
        return True


