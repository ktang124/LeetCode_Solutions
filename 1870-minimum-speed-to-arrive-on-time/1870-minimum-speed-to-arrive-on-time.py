class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 1000000000
        if hour <= len(dist)-1:
            return -1
        def canReach(dist, speed, hour):
            time = 0
            for i in range(len(dist)-1):
                curTime = dist[i]//speed
                if (dist[i] % speed != 0):
                    curTime += 1
                time += curTime
                
            time += (dist[-1]/speed)
            return time <= hour
                
        while left < right:
            mid = left + (right - left) // 2
            if canReach(dist, mid, hour):
                right = mid
            else:
                left = mid + 1
                
        return left