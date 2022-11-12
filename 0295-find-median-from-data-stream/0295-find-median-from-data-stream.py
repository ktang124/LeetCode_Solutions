from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        #naive solution
        self.stream = SortedList()

    def addNum(self, num: int) -> None:
        self.stream.add(num)

    def findMedian(self) -> float:
        n = len(self.stream)
        if n % 2 == 0:
            median = self.stream[n//2] + self.stream[(n//2)-1]
            return median/2
        else:
            median = self.stream[n//2]
            return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()