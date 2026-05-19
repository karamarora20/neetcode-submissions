class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxx=0
        for num in numset:
            # print(num)
            if num-1 not in numset:
                l=1
                curr=num
                while curr+1 in numset:
                    l+=1
                    curr+=1
                maxx=max(l,maxx)
        return maxx
        


        