class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * (target+1) for i in range(n+1)]
        dp[0][0] = 1
        #try to get to index 0
        mod = 10**9+7
        def dfs(n, k, target, dp):
            #base case
            if target < 0:
                return 0
            if n == 0:
                return (1 if target == 0 else 0)
            if dp[n][target] != -1:
                return dp[n][target]
                
            total = 0
            for i in range(1,k+1):
                total += dfs(n-1, k, target-i, dp)
            
            dp[n][target] = total
            return total
        
        res = (dfs(n,k,target, dp) % mod)
        return res
        