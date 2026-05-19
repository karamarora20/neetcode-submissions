class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s=i+1
            e=n-1
            while(s<e):
         
                if nums[s]+nums[e]==-nums[i]:
                    ans.append([nums[i],nums[s],nums[e]])
                    s+=1
                    e-=1
                    
                    while s<e and nums[e]==nums[e+1]:
                        e-=1
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
                elif nums[e]+nums[s]<-nums[i]:
                    s+=1
                else:
                    e-=1
  
        return list(ans)
                    
                


