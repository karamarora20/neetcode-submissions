class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n=len(triplets)
        good = [False, False, False]
        
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                
                if t[0] == target[0]:
                    good[0] = True
                if t[1] == target[1]:
                    good[1] = True
                if t[2] == target[2]:
                    good[2] = True
        return all(good)
