class StockSpanner:

    def __init__(self):
        #list of 7 items
        self.monoStack = []

    def next(self, price: int) -> int:
        #create a monotonic stack of decreasing prices
        sumPop = 1
        while self.monoStack and price >= self.monoStack[-1][0]:
            sumPop += self.monoStack.pop()[1]
        self.monoStack.append((price,sumPop))
        return sumPop
        #100, 80, 60, 70, 60, 75, 85
        #1,  1,   1,  2,  1,   
        #100, 80, 60, 70, 60, 75, 85


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)