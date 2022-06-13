class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #encode each of the strings into int time
        timeList = list()
        for time in timePoints:
            hours = int(time[0:2])
            minutes = int(time[3:5])
            encode = (hours * 60) + minutes
            timeList.append(encode)
            #original time
            #upper bound is 24*60 or 1440
            #add or subtract 12*60 or 720 for am and pm

                 
        timeList.sort()
        diff = 2000
        for idx in range(1, len(timeList)):
            smallTime = timeList[idx-1]
            bigTime = timeList[idx]
            diff = min(bigTime - smallTime, diff)
            
        diff = min(diff, 1440 - timeList[-1] + timeList[0]) #calc final point
            
        return diff