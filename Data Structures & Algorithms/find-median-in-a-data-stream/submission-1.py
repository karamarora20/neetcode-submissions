import heapq
class MedianFinder:

    def __init__(self):
        self.max_h_left=[]
        self.min_h_right=[]
        self.n=0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_h_left, -num)
        heapq.heappush(self.min_h_right, -heapq.heappop(self.max_h_left))
        if len(self.min_h_right) > len(self.max_h_left):
            heapq.heappush(self.max_h_left, -heapq.heappop(self.min_h_right))
        

    def findMedian(self) -> float:
        if len(self.min_h_right) < len(self.max_h_left):
            median= -(self.max_h_left[0])
        else:
            median= (self.min_h_right[0] -self.max_h_left[0])/2.0
        return median
        
        