class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for i in range(n)]
        prev_2=nums[0]
        if n==1:
            return prev_2
        prev_1=max(nums[0],nums[1])
        if n==2:
            return prev_1
        for i in range(2,n):
            curr= max(nums[i]+prev_2,prev_1)
            prev_2=prev_1
            prev_1=curr

        return prev_1