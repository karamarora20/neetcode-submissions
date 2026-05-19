from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        freq=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            buckets[count].append(num)

        ans=[]

        for i in range(len(nums),-1,-1):
            ans+=buckets[i]
            if len(ans)==k:
                return ans           

        return ans
         