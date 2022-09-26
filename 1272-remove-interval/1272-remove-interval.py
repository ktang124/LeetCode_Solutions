class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        lBound, rBound = toBeRemoved
        for interval in intervals:
            #case 1, not in lBound
            l,r = interval
            if l >= lBound and r <= rBound:
                continue
            elif l < lBound and r > rBound:
                res.append([l,lBound])
                res.append([rBound,r])
            elif r <= lBound or l >= rBound:
                res.append(interval)
            
            elif r <= rBound and r >= lBound:
                interval[1] = lBound
                res.append(interval)
            elif l >= lBound and l <= rBound:
                interval[0] = rBound
                res.append(interval)
                #one of them is different
             
        return res
            