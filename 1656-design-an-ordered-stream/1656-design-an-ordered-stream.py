class OrderedStream:

    def __init__(self, n: int):
        self.point = 0
        self.lst = [''] * n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey-1] = value
        res = []
        while self.point < len(self.lst) and self.lst[self.point] != '':
            res.append(self.lst[self.point])
            self.point += 1
            
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)