class MedianFinder:
    
    def __init__(self):
        self.small = []
        self.large = [] 

    def addNum(self, num: int) -> None: # log(logn)
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float: # log(1)
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]


'''
    Idea
        1. using two heap(min, max) for adding num => O(logn)
            find median with heapMin[0] & heapMax[0] => O(1)
    Implem
        1. addNum
            create small(max-hip) and large(min-heap)
            add num to small if size is equal, and add largest num of samll to large
            add num to large if size is not equal, and add smallest num of large to small
            size small, large (k, k)
            size small, large (k, k + 1)
        2. findMedian
            if size is equal = (small[0] + large[0]) / 2
            if size is not equl = large[0]


'''

'''        
    # sort array method
    def __init__(self):
        self.dataStream = []
        self.isSorted = False
        self.median = None

    def addNum(self, num: int) -> None: # log(1)
        if num is not None:
            self.dataStream.append(num)
            self.isSorted = False
        
    def findMedian(self) -> float: # log(nlogn)
        if not self.dataStream:
            return None
        if not self.isSorted:
            self.dataStream.sort()
            self.isSorted = True
        size = len(self.dataStream)
        if size % 2 == 0: # even
            self.median = (self.dataStream[size // 2 - 1] + self.dataStream[size // 2]) / 2
        else: # odd
            self.median = self.dataStream[size // 2]
        return self.median
'''


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()