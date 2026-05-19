class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g=defaultdict(list)
        for src,dst in sorted(tickets):
            g[src].append(dst)
        res=["JFK"]
        def dfs(airport):
            if len(res)==len(tickets)+1: # all nodes completed
                return True
            if airport not in g:
                return False
            temp=g[airport]
            for i,v in enumerate(temp):
                g[airport].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                g[airport].insert(i,v)
                res.pop()
        dfs('JFK')
        return res

