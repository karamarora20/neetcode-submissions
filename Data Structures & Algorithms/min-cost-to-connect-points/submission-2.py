class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        vis=set()
        n=len(points)
        heap=[(0,(points[0][0],points[0][1]))]
        total_cost=0
        while(len(vis)<n):
            cost,curr=heapq.heappop(heap)
            if curr in vis:
                continue
            total_cost+=cost
            vis.add(curr)
            
            for point in points:
                x,y=point
                if (x,y) in vis:
                    continue
                i,j=curr
                dist= abs(x-i)+abs(y-j)
                heapq.heappush(heap,(dist,(x,y)))
                
        return total_cost
                
