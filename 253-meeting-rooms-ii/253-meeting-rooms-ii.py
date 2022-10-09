class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_count = 0
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts.sort()
        ends.sort()
        sP = 0
        eP = 0
        count = 0
        n = len(starts)
        while sP < n:
            if starts[sP] <ends[eP]:
                #meeting started
                count += 1
                sP+=1
                max_count = max(count,max_count)
            else:
                #meeting ended
                eP+=1
                count -= 1
                
        return max_count