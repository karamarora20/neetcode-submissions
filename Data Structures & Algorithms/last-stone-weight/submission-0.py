import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_copy=stones[:]
        stones=[]
        for stone in stones_copy:
            heapq.heappush(stones,-stone)
        while(len(stones)>1):
            stone1,stone2=-heapq.heappop(stones),-heapq.heappop(stones)
            if stone1==stone2:
                continue
            if stone1<stone2:
                heapq.heappush(stones,-(stone2-stone1))
            else:
                heapq.heappush(stones,-(stone1-stone2))
        if stones:
            return -stones[0]
        return 0