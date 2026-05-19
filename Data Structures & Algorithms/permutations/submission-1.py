class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        n=len(nums)
        def get_p(l,state,vis):
            if l==n:
                permutations.append(state)
            for i in range(n):
                if not vis[i]:
                    vis[i]=True
                    get_p(l+1,state+[nums[i]],vis)
                    vis[i]=False
        get_p(0,[],[False for _ in range(n)])
        return permutations


                
            