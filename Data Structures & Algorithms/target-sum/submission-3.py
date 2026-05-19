class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        ans=0
        offset = 1000
        dp = [[0] * 2001 for _ in range(n + 1)]

        dp[0][offset]=1
        for i in range(1,n+1):
            for s in range(-1000, 1001):
                if dp[i - 1][s + offset] != 0:
                    dp[i][s + nums[i - 1] + offset] += dp[i - 1][s + offset]
                    dp[i][s - nums[i - 1] + offset] += dp[i - 1][s + offset]
       
        if abs(target) > 1000:
            return 0
        
        return dp[n][target + offset]

        # return dfs(0,0)
        # return ans
            