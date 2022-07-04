class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #at each step, you are making a decision on which color to choose, this means there are 2^n total outcomes
        cache = [[0] * 3 for i in range(len(costs))]
        ans1 = self.dfs(costs, len(costs)-1, 0, cache)
        ans2 = self.dfs(costs, len(costs)-1, 1, cache)
        ans3 = self.dfs(costs, len(costs)-1, 2, cache)
        return min(ans1,ans2,ans3)
    
    def dfs(self, costs, index, prev, cache):
        if(index == -1):
            return 0
        
        if (cache[index][prev] != 0):
            return cache[index][prev]
        
        if prev == 0: #cannot use red
            useBlue = costs[index][1] + self.dfs(costs,index-1,1,cache)
            useGreen = costs[index][2] + self.dfs(costs,index-1,2,cache)
            
            minCost = min(useBlue,useGreen)
            cache[index][prev] = minCost
            return minCost
        elif prev == 1: #cannot use blue
            useRed = costs[index][0] + self.dfs(costs,index-1,0,cache)
            useGreen = costs[index][2] + self.dfs(costs,index-1,2,cache)
            
            minCost = min(useRed, useGreen)
            cache[index][prev] = minCost
            return minCost
        elif prev == 2: #cannot use green
            useRed = costs[index][0] + self.dfs(costs,index-1,0,cache)
            useBlue = costs[index][1] + self.dfs(costs,index-1,1,cache)
            
            minCost = min(useBlue,useRed)
            cache[index][prev] = minCost
            return minCost
       