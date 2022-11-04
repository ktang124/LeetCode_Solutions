class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        #you have options: either take the regular or take the express with the express cost but in the future, it may be cheaper to stay on express
        #states, you are in express or not in express, (True,false), the stop you are at
        n = len(regular)
        dp = [[0,0] for _ in range(len(regular)+1)]
        dp[0][True] = expressCost
        for i in range(1,n+1):
            #we are on express for going to i, where could we have come from
            dp[i][True] = min(dp[i-1][False] + expressCost+express[i-1], dp[i-1][True]+express[i-1])
            dp[i][False] = min(dp[i-1][False] + regular[i-1], dp[i-1][True] + regular[i-1])
        
        return [min(x,y) for x,y in dp[1:]]