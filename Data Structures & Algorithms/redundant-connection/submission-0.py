from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vis=set()
        g=defaultdict(list)
        cycle_start=-1
        cycle=set()
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(parent,node):
            nonlocal cycle_start
            if node in vis:
                cycle_start=node
                return True
            vis.add(node)
            for nei in g[node]:
                if nei==parent:
                    continue
                if dfs(node,nei):
                    if cycle_start!=-1:
                        cycle.add(node)
                    if node == cycle_start:
                        cycle_start=-1
                    return True
            return False
        dfs(-1,1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]

