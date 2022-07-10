class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        return min(self.dfs(cost, len(cost)-1, dp),self.dfs(cost, len(cost)-2, dp))
        
    def dfs(self, cost, i, dp):
        if i < 0:
            return 0
        if dp[i] != 0:
            return dp[i]
        minCost = cost[i] + min(self.dfs(cost,i-1,dp), self.dfs(cost,i-2,dp))
        dp[i] = minCost
        return minCost