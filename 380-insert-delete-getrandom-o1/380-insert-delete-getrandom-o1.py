class RandomizedSet:

    def __init__(self):
        self.randSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randSet:
            return False
        self.randSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randSet:
            self.randSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand = randint(0,len(self.randSet)-1)
        lst = list(self.randSet)
        return lst[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()