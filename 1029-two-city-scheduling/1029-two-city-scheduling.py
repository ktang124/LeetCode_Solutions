class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        total = 0
        #want to keep track of the differences and try to maximize diffs between A and B
        #assume everyone is going to A
        aTotal = sum(a[0] for a in costs)
        #figure out how much you can save by switching n people to B
        diffList = [(a[0]-a[1]) for a in costs]
        diffList.sort(reverse = True)
        diffList= diffList[0:n]
        savings = sum(diffList)
        return aTotal -savings
        
        