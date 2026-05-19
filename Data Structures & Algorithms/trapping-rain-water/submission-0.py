class Solution:
    def trap(self, height: List[int]) -> int: 
        n=len(height)
        max_r=[-1]*n
        max_l=[-1]*n
        max_l[0]=height[0]
        max_r[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
                max_r[i]=max(max_r[i+1],height[i])
        for i in range(1,n,1):
                max_l[i]=max(max_l[i-1],height[i])
        i=0
        water=0
        while(i<n):
            water+= min(max_l[i],max_r[i])-height[i]
            i+=1
        return water
            


                
