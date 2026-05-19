class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        maxArea=0
        while(l<r):
            if heights[l]<=heights[r]:
                area=heights[l]*(r-l)
                l+=1
            else:
                area=heights[r]*(r-l)
                r-=1
            maxArea=max(maxArea,area)

        return maxArea
            