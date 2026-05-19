class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        maxx=max(nums)
        minn=min(nums)
        seq=[0 for i in range(minn,maxx+1)]
        for i in nums:
            seq[i-minn]=1
        c=0
        max_c=0
        for val in seq:
            # print(val)
            if val==1:
                c+=1
                max_c=max(max_c,c)
            else:
                # max_c=max(max_c,c)
                c=0
        return max_c

        