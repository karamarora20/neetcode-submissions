"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new={}
        vis=set([node])
        q=deque([node])
        if not node : return None
        while(q):
            curr=q.popleft()
            if curr not in old_to_new:
                old_to_new[curr]=Node(curr.val)
            for nei in curr.neighbors:
                if nei not in vis:
                    vis.add(nei)
                    q.append(nei)
        q=deque([node])
        vis=set([node])
        while(q):
            curr=q.popleft()
            new_neighbors=[]
            for nei in curr.neighbors:
                new_neighbors.append(old_to_new[nei])
                if nei not in vis:
                    vis.add(nei)
                    q.append(nei)

            old_to_new[curr].neighbors=new_neighbors   
        return old_to_new.get(node)
                



        