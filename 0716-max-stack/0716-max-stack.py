from sortedcontainers import SortedList, SortedSet, SortedDict
class MaxStack:

    def __init__(self):
        self.numToIndex = SortedList(key = lambda x: x[0])
        self.indexToNum = SortedList(key = lambda x : x[0])
        self.index = 0

    def push(self, x: int) -> None:
        #index of the sort
        self.indexToNum.add((self.index, x))
        self.numToIndex.add((x,self.index))
        self.index += 1
       
    def pop(self) -> int:
        i, val = self.indexToNum.pop()
        self.numToIndex.remove((val,i))
        return val
        
    def top(self) -> int:
        i,val = self.indexToNum[-1]
        return val

    def peekMax(self) -> int:
        val, i = self.numToIndex[-1]
        return val
        

    def popMax(self) -> int:
        val, i = self.numToIndex.pop()
        self.indexToNum.remove((i,val))
        
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()