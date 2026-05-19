class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre_prod=[1]*(n)
        suff_prod=[1]*(n)
        ans=[]
        for i in range(1,n):
            pre_prod[i]=pre_prod[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suff_prod[j]=suff_prod[j+1]*nums[j+1]

        for i in range(n):
            ans.append(pre_prod[i]*suff_prod[i])
        return ans

            
