class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        n=len(nums)
        def get_p(l,state,vis):
            if l==n:
                permutations.append(state)
            for i in range(n):
                if nums[i] not in vis:
                    vis.add(nums[i])
                    get_p(l+1,state+[nums[i]],vis)
                    vis.remove(nums[i])
        get_p(0,[],set([]))
        return permutations


                
            