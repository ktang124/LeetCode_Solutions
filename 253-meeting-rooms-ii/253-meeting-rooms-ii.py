class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        max_count = 1
        #sort by start time
        sort_intervals = sorted(intervals, key = lambda x: x[0])
        pq = []
        #add the first meeting
        heapq.heappush(pq, sort_intervals[0][1])
        for i in sort_intervals[1:]:
            #If the room due to free up the earliest is free, assign that room to this meeting
            if pq[0] <= i[0]:
                heapq.heappop(pq)
            #If a new room is to be assigned, we add it to the heap
            #If an old room is allocated, then also we have to add to the heap with updated end time
            heapq.heappush(pq, i[1])
            max_count = max(len(pq),max_count)
                
        return max_count