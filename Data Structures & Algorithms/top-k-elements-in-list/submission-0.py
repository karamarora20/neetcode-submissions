import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        freq=Counter(nums)
        for num,count in freq.items():
            heapq.heappush(heap,[-count,num])
        ans=[]
        while(k>0):
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans
         