class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        def rob_house(start,end):
            n=end-start+1
            dp=[0 for i in range(n+1)]
            dp[1]=nums[start]
            for i in range(start+2,start+n+1):
                idx=i-start
                dp[idx]=max(dp[idx-1],nums[i-1]+dp[idx-2])
            
            return dp[n]
        if l<2:
            return nums[0]
        profit_0=rob_house(0,l-2)
        profit_1=rob_house(1,l-1)
            

        return max(profit_0,profit_1)
        