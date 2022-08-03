class MyCalendar:
    
    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            startWrong = (interval[0] < end and start < interval[1])
            
            if startWrong:
                return False
            
        self.intervals.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)