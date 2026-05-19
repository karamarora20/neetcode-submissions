class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        vis=set()
        cycle=set()
        def get_cycle(node,parent):
            if not node:
                return False
            if node in vis:
                return True
            vis.add(node)
            for nei in g[node]:
                if nei!=parent:
                    if get_cycle(nei,node):
                        cycle.add(nei)
                        return True
            return False
        print(get_cycle(1,-1),cycle)
        for u,v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u,v]

            