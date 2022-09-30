class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}
        self.times = {} 

    def checkIn(self, ID: int, stationName: str, t: int) -> None:
        self.checkIns[ID] = (stationName, t)

    def checkOut(self, ID: int, stationName: str, t: int) -> None:
        startStation, prevT = self.checkIns[ID]
        startEnd = (startStation, stationName)
        diff = t-prevT
        if startEnd not in self.times:
            self.times[startEnd] = (diff,1)
        else:
            curSum, num = self.times[startEnd]
            curSum += diff
            num += 1
            self.times[startEnd] = (curSum,num)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        curSum, num = self.times[key]
        return float(curSum/num)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)