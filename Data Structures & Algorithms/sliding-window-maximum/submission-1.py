import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        heap=[]
        ans=[]
        for i in range(n):
            while(heap and heap[0][1]<=i-k):
                heapq.heappop(heap)
            heapq.heappush(heap,(-nums[i],i))
            if i>=k-1:
                ans.append(-heap[0][0])
        return ans
