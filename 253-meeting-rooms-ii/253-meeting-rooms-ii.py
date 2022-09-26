class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [intervals[i][0] for i in range(len(intervals))]
        ends = [intervals[i][1] for i in range(len(intervals))]
        starts.sort()
        ends.sort()
        sPoint = 0
        ePoint = 0
        maximum = 1
        curCount = 0
        while sPoint < len(intervals):
            
            
            if starts[sPoint] < ends[ePoint]:
                curCount += 1
                sPoint += 1
            else:    
                ePoint += 1
                curCount -= 1
            maximum = max(maximum, curCount)
            
        return maximum