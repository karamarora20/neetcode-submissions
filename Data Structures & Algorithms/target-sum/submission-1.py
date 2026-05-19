class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        ans=0
        dp=[[float('inf') for _ in range(-1000,1001)] for _ in range(n)]
        def dfs(idx,cur_sum):
            if idx==n:
                if cur_sum==target:
                    return 1
                return 0
            pos=dfs(idx+1,cur_sum+nums[idx])
            neg=dfs(idx+1,cur_sum-nums[idx])
            return pos+neg
        return dfs(0,0)
        # return ans
            