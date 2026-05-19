class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx=0
        n=len(heights)
        s=0
        e=n-1
        while(s<e):
            area=min(heights[s],heights[e])*(e-s)

            maxx=max(area,maxx)
            if heights[s]<heights[e]:
                s+=1
            elif heights[s]>heights[e]:
                e-=1
            elif heights[s]==heights[e]:
                s+=1
        return maxx