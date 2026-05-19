class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0 for _ in range(amount+1)] for _ in range(n+1)]
        def dfs(idx,target):
            if target==0:
                return 0
            if target<0 or idx==n:
                return float('inf')
            if dp[idx][target]!=0:
                return dp[idx][target]
            take=1+dfs(idx,target-coins[idx])
            not_take=dfs(idx+1,target)
            dp[idx][target]=min(take,not_take)
            return dp[idx][target]
        ans=dfs(0,amount)
        return ans if ans!=float('inf') else -1
            