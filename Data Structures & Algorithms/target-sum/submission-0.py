class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        ans=0
        def dfs(idx,cur_sum):
            if idx==n:
                if cur_sum==target:
                    nonlocal ans
                    ans+=1
                return
            dfs(idx+1,cur_sum+nums[idx])
            dfs(idx+1,cur_sum-nums[idx])
        dfs(0,0)
        return ans
            