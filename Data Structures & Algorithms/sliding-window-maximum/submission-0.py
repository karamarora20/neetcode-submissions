class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[]
        print(n)
        for i in range(0,n-k+1):
            maxx=-10001
            for j in range(k):
                maxx=max(maxx,nums[i+j])
            ans.append(maxx)
        return ans
