class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.iterator = []
        for i in range(len(vec)):
            for j in range(len(vec[i])):
                self.iterator.append(vec[i][j])
                
        self.index = 0

    def next(self) -> int:
        res = self.iterator[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < len(self.iterator)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()