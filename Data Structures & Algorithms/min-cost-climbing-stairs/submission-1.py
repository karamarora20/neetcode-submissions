class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        # dp=[0 for _ in range(n+1)]
        a,b=0,0
        for i in range(2,n+1):
            a,b= min(a+cost[i-1],b+cost[i-2]),a
        return a