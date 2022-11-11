class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sortSat = sorted(satisfaction)
        #want to include as many dishes as possible to increase multiplier on the last element
        #choose to start at any point
        maximum = 0
        for start in range(len(sortSat)):
            _sum = 0
            multiplier = 1
            for i in range(start, len(sortSat)):
                _sum += sortSat[i] * multiplier
                multiplier += 1
            maximum = max(_sum,maximum)
        return maximum
                