class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        res=[]
        n=len(nums)
        def dfs(idx,target,used):
            if target==0:
                res.append(used)
                return
            if target<0 or idx>=n:
                return
            dfs(idx,target-nums[idx],used+[nums[idx]])
            dfs(idx+1,target,used)
        dfs(0,target,[])
        return res