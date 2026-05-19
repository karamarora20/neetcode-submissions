class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            time=0
            for b in piles:
                time+=b//k
                time+=1 if b%k>0 else 0
            return time<=h
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            if can_eat(mid):
                high=mid-1
            else:
                low=mid+1
        return low