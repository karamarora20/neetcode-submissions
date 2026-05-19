class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # used=[False for _ in candidates]
        candidates.sort()
        res=[]
        n=len(candidates)
        def dfs(idx,target,nums):
            if target==0:
                res.append(nums)
                return
            if target<0 or idx>=n :
                return
            
            dfs(idx+1,target-candidates[idx],nums+[candidates[idx]])
            while idx + 1 < n and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1,target,nums)
        dfs(0,target,[])
        return res