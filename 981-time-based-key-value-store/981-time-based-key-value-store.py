class TimeMap:

    def __init__(self):
        self.map = defaultdict(lambda: [])
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map[key]
        if len(lst) == 0:
            return ""
        #binary search for the timestamp
        left = 0
        right = len(lst)-1
        while left <= right:
            mid = left + (right - left)//2
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            elif lst[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid-1
                
        if lst[right][0] < timestamp:
            return lst[right][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)