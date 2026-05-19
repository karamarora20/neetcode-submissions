class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        # Build adjacency list
        for u, v, t in times:
            graph[u].append((v, t))
        
        # Min heap: (current_time, node)
        heap = [(0, k)]
        dist = {}
        
        while heap:
            time, node = heapq.heappop(heap)
            
            # Skip if already visited
            if node in dist:
                continue
                
            dist[node] = time
            
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + wt, nei))
        
        # If not all nodes reached
        if len(dist) != n:
            return -1
        
        return max(dist.values())